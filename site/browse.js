// /browse/: faceted filtering, AND across facets, state in the URL (?topic=inflation&school=austrian&format=lecture).
(async () => {
  const $ = s => document.querySelector(s);
  const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const [{ items }, F] = await Promise.all([fetch("/data/videos.json").then(r => r.json()), fetch("/data/facets.json").then(r => r.json())]);
  const L = F.labels;
  const FACETS = [ // url key, label, getter, label map
    ["kind", "Media", it => [it.kind], { video: "Video", audio: "Audio" }],
    ["topic", "Topic", it => it.t, L.topics], ["field", "Field", it => it.f, L.fields], ["school", "School", it => it.s, L.schools],
    ["format", "Format", it => it.fm ? [it.fm] : [], L.formats], ["level", "Level", it => it.l ? [it.l] : [], L.levels],
    ["era", "Era covered", it => it.e, L.eras], ["region", "Region", it => it.r, L.regions],
    ["len", "Length", it => { const d = +it.duration || 0; return d ? [d < 1200 ? "short" : d <= 3600 ? "mid" : "long"] : [] }, { short: "< 20 min", mid: "20–60 min", long: "60+ min" }],
    ["lang", "Language", it => [(it.lang || "en").slice(0, 2)], { en: "English", pl: "Polish" }],
  ];
  const sel = () => { const p = new URLSearchParams(location.search), m = {}; FACETS.forEach(([k]) => { const v = p.getAll(k); if (v.length) m[k] = v }); return m };
  const match = (it, m, skip) => FACETS.every(([k, , get]) => k === skip || !m[k] || m[k].every(v => get(it).includes(v)));
  const thumb = it => it.kind === "audio" ? it.art : `https://i.ytimg.com/vi/${it.id}/hq2.jpg`;

  function render() {
    const m = sel(), hits = items.filter(it => match(it, m));
    $("#facets").innerHTML = FACETS.map(([k, label, get, map]) => {
      const c = {}; items.filter(it => match(it, m, k)).forEach(it => get(it).forEach(v => c[v] = (c[v] || 0) + 1));
      const rows = Object.entries(c).sort((a, b) => b[1] - a[1]).slice(0, k === "topic" ? 40 : 15);
      if (!rows.length) return "";
      return `<details ${innerWidth > 800 || m[k] ? "open" : ""}><summary>${label}</summary>` + rows.map(([v, n]) =>
        `<label><input type="checkbox" data-k="${k}" value="${esc(v)}" ${m[k]?.includes(v) ? "checked" : ""}> ${esc(map?.[v] || v)} <small>${n}</small></label>`).join("") + "</details>";
    }).join("");
    $("#active").innerHTML = `${hits.length} items` + (Object.keys(m).length ? ' · <a href="/browse/">clear</a>' : "");
    $("#bgrid").innerHTML = hits.slice(0, 200).map(it => `<a class="card" href="/v/${it.id}/"><div class="th"><img loading="lazy" src="${esc(thumb(it))}" alt=""></div>
      <h3>${esc(it.title)}</h3><div class="meta">${esc(it.channel)}${it.published ? " · " + it.published.slice(0, 4) : ""}</div></a>`).join("") || '<p class="empty">Nothing matches all filters.</p>';
  }
  $("#facets").addEventListener("change", ev => {
    const p = new URLSearchParams(location.search), { k } = ev.target.dataset, v = ev.target.value;
    const cur = p.getAll(k).filter(x => x !== v); p.delete(k); (ev.target.checked ? [...cur, v] : cur).forEach(x => p.append(k, x));
    history.replaceState(null, "", "?" + p.toString()); render();
  });
  render();
})();
