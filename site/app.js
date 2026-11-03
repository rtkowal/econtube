// EconTube client: tabs, filters, search, For You (localStorage only), keyboard shortcuts.
(() => {
  const $ = (s, e = document) => e.querySelector(s), $$ = (s, e = document) => [...e.querySelectorAll(s)];
  const store = { get(k, d) { try { return JSON.parse(localStorage.getItem("et:" + k)) ?? d } catch { return d } },
                  set(k, v) { try { localStorage.setItem("et:" + k, JSON.stringify(v)) } catch {} } };
  const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ---- item page: record watch, thumbs ----
  const page = document.body.dataset.item;
  if (page) {
    const seen = store.get("seen", []); if (!seen.includes(page)) { seen.push(page); store.set("seen", seen.slice(-2000)) }
    const aff = store.get("aff", {}), ch = document.body.dataset.channel;
    aff[ch] = (aff[ch] || 0) + 1; store.set("aff", aff);
    const votes = store.get("votes", {});
    $$(".thumbs button").forEach(b => {
      b.setAttribute("aria-pressed", votes[page] === +b.dataset.v);
      b.onclick = () => { votes[page] = votes[page] === +b.dataset.v ? 0 : +b.dataset.v; store.set("votes", votes);
        aff[ch] = (aff[ch] || 0) + 3 * (votes[page] || 0); store.set("aff", aff);
        $$(".thumbs button").forEach(x => x.setAttribute("aria-pressed", votes[page] === +x.dataset.v)) };
    });
  }

  // ---- home grid ----
  const grid = $("#grid"); if (!grid) return;
  let DATA = [], tab = location.hash.slice(1) || "top", kind = store.get("kind", "all"), q = "", sel = -1;
  const fmtDur = s => { if (!s) return ""; if (/:/.test(s)) return s.replace(/^0(?=\d:)/, ""); s = +s; if (!s) return "";
    const h = s / 3600 | 0, m = (s % 3600) / 60 | 0; return h ? `${h}:${String(m).padStart(2, "0")}:00` : `${m} min` };
  const via = it => { const n = [...new Set(it.sources.map(s => s.name))]; return "via " + n.slice(0, 2).join(", ") + (n.length > 2 ? ` +${n.length - 2}` : "") };
  const thumb = it => it.kind === "audio" ? it.art : `https://i.ytimg.com/vi/${it.id}/hq2.jpg`;

  function rank() {
    let L = DATA.filter(it => kind === "all" || it.kind === kind);
    if (q) { const t = q.toLowerCase().split(/\s+/).filter(Boolean);
      L = L.filter(it => { const h = (it.title + " " + it.channel + " " + it.sources.map(s => s.name).join(" ")).toLowerCase(); return t.every(w => h.includes(w)) }) }
    if (tab === "new") L = [...L].sort((a, b) => (b.published || "").localeCompare(a.published || ""));
    if (tab === "foryou") {
      const aff = store.get("aff", {}), seen = new Set(store.get("seen", [])), votes = store.get("votes", {});
      L = L.filter(it => !seen.has(it.id) && votes[it.id] !== -1)
           .map(it => [it, it.score * (1 + Math.log1p(Math.max(0, aff[it.channel] || 0)))]).sort((a, b) => b[1] - a[1]).map(x => x[0]);
    }
    return L;
  }
  function render() {
    $$("nav.tabs a").forEach(a => a.toggleAttribute("aria-current", a.hash === "#" + tab));
    $$(".bar button").forEach(b => b.setAttribute("aria-pressed", b.dataset.k === kind));
    const seen = new Set(store.get("seen", [])), L = rank();
    grid.innerHTML = L.length ? L.slice(0, 240).map(it => `<a class="card${seen.has(it.id) && tab !== "foryou" ? " seen" : ""}" href="/v/${it.id}/">
      <div class="th"><img loading="lazy" src="${esc(thumb(it))}" alt="" onerror="this.onerror=null;this.src='https://i.ytimg.com/vi/${it.id}/hqdefault.jpg'">${it.kind === "audio" ? '<span class="badge">🎧 ' + esc(fmtDur(it.duration)) + "</span>" : ""}</div>
      <h3>${esc(it.title)}</h3><div class="meta">${esc(it.channel)}${it.published ? " · " + it.published.slice(0, 4) : ""}</div>
      <div class="via">${esc(via(it))}</div></a>`).join("") : `<p class="empty">${tab === "foryou" ? "Watch or rate a few things and this tab learns what you like." : "Nothing matches."}</p>`;
    sel = -1;
  }
  fetch("/data/videos.json").then(r => r.json()).then(d => { DATA = d.items; render() });
  addEventListener("hashchange", () => { tab = location.hash.slice(1) || "top"; render() });
  $$(".bar button").forEach(b => b.onclick = () => { kind = b.dataset.k; store.set("kind", kind); render() });
  $("#q").addEventListener("input", e => { q = e.target.value.trim(); render() });
  $("#reset")?.addEventListener("click", e => { e.preventDefault(); ["seen", "aff", "votes"].forEach(k => store.set(k, k === "seen" ? [] : {})); render() });

  addEventListener("keydown", e => {
    if (e.target.tagName === "INPUT") { if (e.key === "Escape") e.target.blur(); return }
    const cards = $$(".card");
    if (e.key === "/") { e.preventDefault(); $("#q").focus() }
    else if (e.key === "j" || e.key === "k") { sel = Math.max(0, Math.min(cards.length - 1, sel + (e.key === "j" ? 1 : -1)));
      cards.forEach((c, i) => c.classList.toggle("sel", i === sel)); cards[sel]?.scrollIntoView({ block: "nearest" }) }
    else if (e.key === "Enter" && sel >= 0) cards[sel].click();
    else if (e.key === "?") $("#help").classList.toggle("on");
    else if (e.key === "t") location.href = "/sources/";
  });
})();
