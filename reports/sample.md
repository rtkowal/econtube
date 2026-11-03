# Step 2 sample: classification report

Items in catalogue: 173; classified: 173.

## LLM usage this run

| model | step | calls | input tok | output tok |
|---|---|---:|---:|---:|
| gpt-5.4-nano | classify | 346 | 267,876 | 133,924 |
| gpt-5.4-nano | classify-retry | 246 | 203,725 | 93,816 |
| gpt-5.4-nano | gate | 147 | 37,045 | 4,561 |

Multiply by the model's current per-token price to get cost; per-item cost × expected catalogue size = backfill cost.

## Relevance gate

147 gated items, 130 rejected. Rejection reasons (first 25):

- `lizItRX2U2M`: Primarily political analysis of Trump and institutions (conf 0.86)
- `RtfLtMEpee4`: Focuses on US–Africa partnerships; mixed strategic/security politics. (conf 0.73)
- `58OMfCQ_MHQ`: Main topic is U.S. midterm politics, not economics (conf 0.85)
- `KllGJcSgoL4`: Focuses on voter ID and election security, not economics. (conf 0.9)
- `APJ2s-1brjk`: Primary topic is presidential power/history, not economics (conf 0.72)
- `Hhhr0DpLGkI`: Primarily legal privacy debate, not economics (conf 0.78)
- `YXdBzRQUdnQ`: Primarily AI regulation discussion plus riots and partisan politics (conf 0.74)
- `l_q7Ac8Qfrk`: Primarily political history/culture, not economics (conf 0.78)
- `ctNM986_QZ0`: Focuses on geopolitics and war, not economics. (conf 0.72)
- `405UW4L-xwM`: Mostly politics/culture-war; economics only incidental (conf 0.86)
- `qkqtAjhVRSQ`: Mostly healthcare/vaccines and politics, not economics. (conf 0.86)
- `wYYF-2Jsaus`: Partisan politics and culture-war discussion dominates (conf 0.76)
- `jN9Y396WKHs`: Main focus is military history and politics, not economics (conf 0.78)
- `aG1x--6LHiM`: Main subject is politics and conflicts, not economics (conf 0.9)
- `1o_39vY5YM8`: Mostly leadership, institutions, climate rhetoric, sports; not economics (conf 0.78)
- `UjY7YbSc91w`: Primarily constitutional principles, not economics or markets (conf 0.72)
- `mdagfIfrl2g`: Focus on SCOTUS politics and geopolitics, not economics (conf 0.86)
- `SqiEh5Q07u8`: Constitutional debate; politics and governance, not economics. (conf 0.74)
- `7FLY3fO7JJ4`: Primarily partisan politics, not economics or markets. (conf 0.9)
- `iLJB2f5HUeA`: History and political commentary, not economics-focused (conf 0.78)
- `nJ3lO2gg7ek`: Main subject is religion and theology, not economics. (conf 0.95)
- `siDkGU1uVHg`: Founding history and partisan themes, not economics. (conf 0.9)
- `gBEdxb8ei_0`: Focuses on geopolitical leadership, not economics primarily (conf 0.88)
- `--Ef5Q-3Iq8`: Focus is military/defense strategy, not economics. (conf 0.9)
- `Yx9EDpo58rw`: Main topic is partisan politics, not economics. (conf 0.88)

## 50 sample rows

**OpenAI - Fireside Chat with Tyler Cowen and Alex Tabarrok** — Wyatt Thompson · via Marginal Revolution  
why: _A practical economics take on AI’s impact on growth, innovation incentives, and policy tradeoffs._  
field: innovation · topic: ai-economy · school: — · format: interview · level: intermediate · era: 2020s · region: —  
speakers: Tyler Cowen, Alex Tabarrok, Sam Altman · discussed: Elon Musk  
tags: artificial intelligence, economic growth, innovation policy, platform competition, productivity, regulation and ai, startup ecosystem

**Francesco Sabella in Conversation With Victor Niederhoffer: Harvard Legend Hedge Fund Pioneer** — Francesco Sabella · via Marginal Revolution  
why: _Hedge-fund investing insights from a proven trader, with practical perspectives on markets and risk._  
field: markets-investing, finance · topic: — · school: — · format: interview · level: intermediate · era: — · region: us  
speakers: Francesco Sabella, Victor Niederhoffer · discussed: —  
tags: active trading, asset allocation, behavioral finance, harvard, hedge funds, market timing, risk management

**2026, Methods Lecture, Melissa Dell and Ashesh Rambachan, "Estimation and Inference with AI...** — NBER · via Marginal Revolution  
why: _Expert lecture on econometric estimation and inference using AI methods in applied research._  
field: quantitative · topic: ai-economy · school: empirical · format: lecture · level: expert · era: 2020s · region: —  
speakers: Melissa Dell, Ashesh Rambachan · discussed: —  
tags: ai methods, causal inference, econometrics, estimation, inference, machine learning, statistical theory

**A Price Is a Signal Wrapped Up in an Incentive** — Marginal Revolution University · via Marginal Revolution  
why: _Explains how prices convey information and align incentives for efficient decisions._  
field: micro · topic: price-system · school: — · format: — · level: — · era: timeless · region: —  
speakers: — · discussed: —  
tags: incentives, market coordination, opportunity cost, prices as information, resource allocation

**Was the China Shock Overblown? | Russ Roberts and Joseph Francis** — Hoover Institution · via Hoover Institution  
why: _Debates whether the China-shock job-loss story rests on fragile evidence and what that implies for policy._  
field: labor, international, trade · topic: china-economy · school: empirical · format: podcast-episode · level: intermediate · era: 2010s · region: china, us  
speakers: Russ Roberts, Joseph Francis · discussed: David Autor, Daron Acemoglu, Gordon Hanson  
tags: causal inference, china shock, import competition, labor market outcomes, local labor markets, manufacturing employment, offshoring, trade adjustment

**The History of Macroeconomics from Keynes to HANK Models with Greg Kaplan** — Hoover Institution · via Hoover Institution  
why: _An insider tour of macro theory’s evolution to HANK models, with Nobel-related context._  
field: history-of-thought, macro · topic: — · school: keynesian · format: podcast-episode · level: intermediate · era: — · region: —  
speakers: Jon Hartley, Greg Kaplan · discussed: John Maynard Keynes, Robert E. Hall, Michael Woodford  
tags: business cycles, hank models, heterogeneous agent models, macro history, monetary policy transmission, new keynesian, nobel prize, rational expectations

**Has China Become an Innovation Giant?** — Hoover Institution · via Hoover Institution  
why: _Evaluates whether China’s innovation boom is real, and what drives it using evidence._  
field: innovation, international · topic: china-economy · school: — · format: podcast-episode · level: intermediate · era: 2010s · region: china  
speakers: Josh Lerner, Amit Seru, Steven Davis · discussed: —  
tags: catch up growth, chinese innovation, corporate r&d, industrial policy, innovation metrics, productivity, research and development, science and technology

**The Billionaire Tax, The Busted Federal Budget, and the Future of the American Experiment** — Hoover Institution · via Hoover Institution  
why: _Rauh connects the billionaire-tax debate to federal budget math and debt-driven fiscal risk._  
field: fiscal-macro · topic: national-debt, taxation · school: — · format: podcast-episode · level: expert · era: — · region: us  
speakers: Joshua Rauh · discussed: —  
tags: budget deficits, federal debt, fiscal sustainability, government spending, interest costs, political economy, tax policy

**Taxing Billionaires, 9/11, and the Lessons We Forgot** — Hoover Institution · via Hoover Institution  
why: _Wealth-tax proposal and 9/11 lessons are used to discuss fiscal risks and policy tradeoffs._  
field: fiscal-macro · topic: taxation, inequality · school: — · format: podcast-episode · level: — · era: — · region: us  
speakers: — · discussed: —  
tags: 9/11 lessons, fiscal policy, homeland security, inequality, progressive taxation, tax avoidance, tax incidence, wealth tax

**Make IPOs Great Again: SEC Chairman Paul Atkins on Ending Regulation by Enforcement** — Hoover Institution · via Hoover Institution  
why: _SEC leadership argues enforcement-heavy rules suppress IPOs and capital formation._  
field: markets-investing · topic: regulation · school: — · format: interview · level: — · era: timeless · region: us  
speakers: Paul Atkins, Peter Robinson · discussed: Gary Gensler  
tags: capital formation, corporate disclosure, investor protection, ipo regulation, market liquidity, market regulation, sec, securities enforcement

**Thomas Sowell on School Choice and the Price Our Children Pay for Bad Ideas | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _A data-driven critique of education ideology, inequality, and school-choice policy in the US._  
field: health-education-welfare · topic: inequality · school: — · format: lecture · level: intermediate · era: timeless · region: us  
speakers: Thomas Sowell · discussed: Martin Luther King Jr.  
tags: affirmative action, education policy, harlem, ideology vs evidence, school choice, university admissions

**Teaching Gorbachev Capitalism: Powell, Rice, and Boskin Discuss George Shultz, the Economist** — Hoover Institution · via Hoover Institution  
why: _Notable policymakers discuss Shultz’s economic legacy, linking US monetary policy to market reforms abroad._  
field: — · topic: — · school: — · format: panel · level: intermediate · era: — · region: us  
speakers: Jerome Powell, Condoleezza Rice, Michael Boskin · discussed: George P. Shultz, Mikhail Gorbachev, Milton Friedman  
tags: federal reserve, george p. shultz, inflation policy, monetary policy, soviet reforms, supply side economics, tax reform, transition to markets

**Thomas Sowell: A Free Man | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Thomas Sowell explains how markets and incentives shape freedom, policy, and inequality through his life story._  
field: history-of-thought · topic: — · school: classical-liberal · format: — · level: intermediate · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Friedrich Hayek, Milton Friedman  
tags: civil rights, evidence based economics, free markets, inequality of outcomes, limited government, public policy, spontaneous order

**Inflation Is A Choice: Kevin Warsh On Fixing The Federal Reserve | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _A nominee’s critique of the Fed’s inflation performance and proposed reforms to restore stability._  
field: monetary-policy, macro · topic: inflation, the-fed, interest-rates · school: — · format: interview · level: intermediate · era: 2020s · region: us  
speakers: Kevin Warsh · discussed: Donald Trump, Jerome Powell, Federal Reserve  
tags: central bank governance, federal reserve, inflation targeting, interest rate policy, monetary policy credibility, nomination politics, price stability

**Thomas Sowell: Facts Against Rhetoric, Capitalism, Culture and Yes, the Tariffs | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Sowell challenges political rhetoric with evidence, including arguments for and against tariffs._  
field: trade · topic: tariffs · school: classical-liberal · format: interview · level: — · era: — · region: —  
speakers: Thomas Sowell, Peter Robinson · discussed: Donald Trump  
tags: capitalism, comparative advantage, cultural explanations, facts versus rhetoric, free trade, state intervention, tariff incidence, trade policy

**Thomas Sowell Discusses The Trump Tariffs | Uncommon Knowledge | Full Interview on April 15, 2025** — Hoover Institution · via Hoover Institution  
why: _Debates the economic effects of Trump’s tariffs through a strong free-trade critique._  
field: trade · topic: tariffs · school: — · format: interview · level: — · era: 2020s · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: consumer costs, economic incidence, international competition, producer incentives, protectionism, supply chains, tariffs, trade policy

**Doing “The Best Things First,” with Bjorn Lomborg | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _A structured discussion on ranking policies using evidence and cost-benefit reasoning._  
field: environment-energy · topic: — · school: — · format: interview · level: intermediate · era: 2020s · region: global  
speakers: Bjorn Lomborg, D. Bruce Atkinson · discussed: —  
tags: climate policy, copenhagen consensus, cost benefit analysis, prioritization of interventions, public policy

**Consequences Matter: Thomas Sowell on “Social Justice Fallacies” | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques “social justice” policy reasoning through consequences and incentives._  
field: history-of-thought · topic: — · school: classical-liberal · format: podcast-episode · level: — · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: equity vs equality, government programs, market incentives, normative vs positive economics, policy evaluation, social justice, unintended consequences

**The Ethos of Economics with John Cogan and Kevin Warsh** — Hoover Institution · via Hoover Institution  
why: _Policymaker economists discuss how economics should guide efficient, cost-effective governance._  
field: public · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: John Cogan, Kevin Warsh · discussed: —  
tags: cost effectiveness, economic ethos, government efficiency, institutional analysis, policy design

**Thomas Sowell on Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques how expert elites can drive policy disasters, using historical examples._  
field: history-of-thought · topic: — · school: — · format: lecture · level: intermediate · era: timeless · region: us  
speakers: Thomas Sowell · discussed: Franklin D. Roosevelt  
tags: american history, brain trust, expertocracy, institutions, intellectuals, policy failure, public choice

**Thomas Sowell -- Basic Economics** — Hoover Institution · via Hoover Institution  
why: _A clear primer on how prices and incentives coordinate decisions in a market economy._  
field: general · topic: price-system · school: — · format: lecture · level: introductory · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: basic economics, free markets, incentives, market prices, opportunity cost, policy evaluation, scarcity, trade offs

**Thomas Sowell on the second edition of Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _Sowell revisits his core argument on how ideas and elites shape policy and public life._  
field: history-of-thought · topic: — · school: classical-liberal · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: classical liberalism, cultural critique, ideology, intellectuals and society, market institutions, policy debate, public discourse

**Thomas Sowell -- Dismantling America** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques modern American social policy and ideas using economic reasoning and history._  
field: — · topic: — · school: classical-liberal · format: — · level: intermediate · era: — · region: us  
speakers: Thomas Sowell · discussed: —  
tags: book: dismantling america, critical race theory, government intervention, intellectual history, public choice, rule of law, social policy

**An Economist Looks at 90: Thomas Sowell on Charter Schools and Their Enemies** — Hoover Institution · via Hoover Institution  
why: _Sowell explains how charter schools and political opposition shape educational outcomes and opportunities._  
field: — · topic: — · school: — · format: interview · level: intermediate · era: — · region: us  
speakers: Thomas Sowell · discussed: —  
tags: charter schools, education choice, education inequality, government regulation, market competition, school vouchers, us education policy

**Thomas Sowell and a Conflict of Visions** — Hoover Institution · via Hoover Institution  
why: _Offers a framework for understanding how underlying assumptions drive political conflicts._  
field: — · topic: — · school: classical-liberal · format: — · level: intermediate · era: timeless · region: us  
speakers: Thomas Sowell · discussed: —  
tags: classical liberalism, ideology, implicit assumptions, interests vs visions, political philosophy, public choice

**Facts and Fallacies with Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _A clear critique of popular misconceptions linking economics to race and public policy._  
field: general · topic: inequality · school: classical-liberal · format: lecture · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Martin Luther King Jr., Herbert Spencer, Karl Marx  
tags: cultural vs institutional explanations, fallacies and evidence, hoover institution debate, inequality measurement, public policy evaluation, race and economics

**Thomas Sowell discusses his newest book, Intellectuals and Race** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques how elite ideas shape race discourse and broader social outcomes._  
field: history-of-thought · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Thomas Sowell · discussed: John Rawls, Karl Marx, Martin Luther King Jr., W. E. B. Du Bois  
tags: idea driven policy, inequality, intellectuals, race, social philosophy

**Thomas Sowell on the Housing Boom and Bust** — Hoover Institution · via Hoover Institution  
why: _Explains how housing policies and incentives helped drive the boom and deepen the bust._  
field: urban-housing, business-cycles · topic: 2008-crisis, housing · school: — · format: — · level: — · era: 2008-crisis, 2000s · region: us  
speakers: Thomas Sowell · discussed: Barack Obama  
tags: credit booms, financial crisis, government housing policy, housing bubble, moral hazard, mortgage backed securities, mortgage lending, subprime mortgages

**Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _A wide-ranging interview on inequality and class conflict through Sowell’s free-market lens._  
field: history-of-thought · topic: — · school: classical-liberal · format: interview · level: — · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Barack Obama, Ty Cob  
tags: class warfare, free markets, inequality, institutional skepticism, presidential politics, racial justice discourse, social policy

**Wealth, Poverty, and Politics** — Hoover Institution · via Hoover Institution  
why: _Sowell compares global and U.S. poverty using a politics-and-policy lens._  
field: development · topic: inequality · school: — · format: — · level: — · era: timeless · region: global, us  
speakers: Thomas Sowell · discussed: —  
tags: absolute vs relative poverty, income inequality, living standards, politics of welfare, poverty measurement, welfare policy

**Richard Epstein Enriches Us with His Ideas on Inequality, Taxes, Politics, and Health Care** — Hoover Institution · via Hoover Institution  
why: _A clear libertarian-leaning take on inequality, taxes, health care, and market-driven politics._  
field: public · topic: inequality, taxation · school: classical-liberal · format: — · level: intermediate · era: — · region: us  
speakers: Richard A. Epstein · discussed: Donald Trump, Barack Obama  
tags: free markets, gay marriage, globalization, healthcare reform, inequality, limited government, tax policy

**First reactions | Michael Woodford, prize in economic sciences 2026 | Telephone interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _A candid interview reacting to the economics Nobel, offering first impressions from a leading economist._  
field: — · topic: — · school: — · format: interview · level: — · era: — · region: —  
speakers: Michael Woodford · discussed: —  
tags: expectations, nobel prize in economic sciences, stockholm announcement, telephone interview

**Announcement of the 2026 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Award announcement highlighting core work linking micro foundations to stabilization in macroeconomics._  
field: macro, micro · topic: — · school: — · format: — · level: — · era: — · region: —  
speakers: Royal Swedish Academy of Sciences · discussed: Robert E. Hall, Michael Woodford, Alfred Nobel  
tags: dynamic stochastic optimization, expectations, general equilibrium, inflation control, macroeconomic stabilization, microeconomic foundations, monetary transmission

**“One of the biggest policy questions we have in macroeconomics.” | 2026 economic sciences interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Interview about rebuilding macro tools for studying business cycles and stabilization policy._  
field: business-cycles, macro · topic: — · school: — · format: interview · level: — · era: 2020s · region: global  
speakers: Timo Boppart, Owen Gaffney · discussed: —  
tags: business cycle modeling, macroeconomic framework rebuilding, macroeconomic stabilization, policy evaluation, stabilization policy

**Roman Mars on Flags, Phones, and the Design of Everyday Life** — Conversations with Tyler · via Conversations with Tyler  
why: _Explores how small design choices shape behavior and institutions in daily life._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Roman Mars, Tyler Cowen · discussed: —  
tags: design, everyday technology, information signals, public space, urban planning

**Liaquat Ahamed on Financial Crises, Gold, and the Lessons of 1873** — Conversations with Tyler · via Conversations with Tyler  
why: _A historically grounded conversation linking the 1873 crisis, central banking, and gold-era financial fragility._  
field: economic-history · topic: great-depression, gold-standard · school: — · format: podcast-episode · level: intermediate · era: pre-1900 · region: global  
speakers: Tyler Cowen, Liaquat Ahamed · discussed: Rothschild family, Central banks  
tags: 1873 panic, banking cartel, central banking, financial crises, gold standard, international capital flows, lenders of last resort, lords of finance, pulitzer prize

**Luis Garicano on Spain, Europe, and the Future of Work** — Conversations with Tyler · via Conversations with Tyler  
why: _Garicano connects European labor-market challenges with AI-driven restructuring and productivity prospects._  
field: innovation · topic: ai-economy · school: — · format: interview · level: intermediate · era: — · region: eurozone  
speakers: Luis Garicano, Tyler Cowen · discussed: Gary Becker, Kevin Murphy, Sherwin Rosen  
tags: ai and productivity, european integration, future of work, labor market, spain economy, task automation, technological change

**Gita Gopinath on Trade, Currencies, and Economic Transformation** — Conversations with Tyler · via Conversations with Tyler  
why: _IMF insider on how currencies and trade shape macro outcomes and economic transformation._  
field: international, trade, intl-finance · topic: — · school: — · format: podcast-episode · level: expert · era: 2020s · region: global  
speakers: Gita Gopinath, Tyler Cowen · discussed: Christine Lagarde  
tags: capital flows, exchange rate regimes, imf, inflation dynamics, monetary transmission, sovereign debt restructuring, trade policy

**Annie Lowrey on the Time Tax, Fraud, and Rationing by Paperwork** — Conversations with Tyler · via Conversations with Tyler  
why: _A sharp look at how administrative hassle operates like regressive taxation, especially for the poor._  
field: public · topic: inequality, regulation · school: — · format: podcast-episode · level: intermediate · era: — · region: us  
speakers: Annie Lowrey, Tyler Cowen · discussed: Anthony Downs  
tags: administrative burden, bureaucratic failure, fraud incentives, paperwork costs, rationing by bureaucracy, regressive policy design, time tax, welfare systems

**Jared Diamond on Leaders, Luck, and Irreplaceability** — Conversations with Tyler · via Conversations with Tyler  
why: _A thought-provoking discussion on whether leaders matter more than contingency and luck._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: pre-1900 · region: global  
speakers: Jared Diamond, Tyler Cowen · discussed: Genghis Khan, Jesus Christ  
tags: historical contingencies, human history, institutional endurance, irreplaceability, leadership, luck vs skills

**Michael Moritz on Origin Stories, Exile, and Obsessive Curiosity** — Conversations with Tyler · via Conversations with Tyler  
why: _A high-signal discussion of entrepreneurship, storytelling, and how major companies evolve._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Michael Moritz, Tyler Cowen · discussed: Steve Jobs, Alex Ferguson  
tags: corporate turnarounds, entrepreneurship, founder narratives, memoir, origin stories, sequoia capital, startup ecosystem, venture capital

**Luke Burgis on Mimetic Desire, Catholicism, and the Age of Social Contagion** — Conversations with Tyler · via Conversations with Tyler  
why: _Explains mimetic desire and social contagion through Girard and Catholic thought for modern behavior._  
field: — · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: global  
speakers: Luke Burgis, Tyler Cowen · discussed: René Girard  
tags: catholicism, cultural evolution, mimetic desire, religious institutions, rené girard, social contagion

**Revisiting the China Shock (with Joseph Francis)** — EconTalk · via EconTalk  
why: _Reassesses evidence behind the China shock and its job-displacement conclusions for U.S. labor markets._  
field: trade, labor · topic: china-economy · school: — · format: podcast-episode · level: intermediate · era: 2000s · region: china, us  
speakers: Joseph Francis, Russ Roberts · discussed: David Autor, David Dorn, Gordon Hanson, Lawrence Katz  
tags: causal inference, china shock, import competition, local labor markets, manufacturing decline, manufacturing employment, offshoring, trade adjustment

**How Your Situation Shapes You (with Angela Duckworth)** — EconTalk · via EconTalk  
why: _Explains how environment and incentives can matter more than grit for habit change and achievement._  
field: behavioral · topic: — · school: behavioral · format: podcast-episode · level: — · era: — · region: —  
speakers: Russ Roberts, Angela Duckworth · discussed: —  
tags: behavior change, grit, habit formation, psychology of incentives, self control, social environment, willpower

**Lives Wasted and Well-Lived: David Wolpe on The Death of Ivan Ilyich** — EconTalk · via EconTalk  
why: _A mortality-focused literary conversation that connects end-of-life reflection with meaning and how we measure lives._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Russ Roberts, David Wolpe · discussed: Leo Tolstoy, Ivan Ilyich  
tags: end of life care, ethical reflection, existential risk, life satisfaction, mortality, tolstoy

**The Great Fertility Collapse (with Jesus Fernandez-Villaverde)** — EconTalk · via EconTalk  
why: _Explains why falling fertility is reshaping growth, labor markets, and welfare worldwide._  
field: development · topic: economic-growth · school: — · format: podcast-episode · level: intermediate · era: 2020s · region: global  
speakers: Jesus Fernández-Villaverde · discussed: —  
tags: childbearing, demographic transition, dependency ratio, economic growth, fertility collapse, labor supply, population aging

**Addiction, Faith, and the Limits of Willpower (with Meghan O'Gieblyn)** — EconTalk · via EconTalk  
why: _Explores addiction as a limits-of-willpower problem using insights from behavioral and moral philosophy._  
field: behavioral · topic: healthcare · school: behavioral · format: podcast-episode · level: — · era: — · region: —  
speakers: Russ Roberts, Meghan O'Gieblyn · discussed: Simone Weil, William James, Iris Murdoch  
tags: addiction, behavioral economics, belief and commitment, faith and doubt, intrinsic motivation, moral psychology, self control, willpower

**Public Choice and Politics Without Romance (with Mike Munger)** — EconTalk · via EconTalk  
why: _A crisp public-choice framework for judging government proposals using political-incentive realism._  
field: public, law-econ · topic: — · school: public-choice · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Mike Munger, Russ Roberts · discussed: James Buchanan, Gordon Tullock  
tags: constitutional political economy, political incentives, principal agent problems, public choice, public policy evaluation, regulatory capture, rent seeking

**The Death of Reading (with James Marriott)** — EconTalk · via EconTalk  
why: _Links declining reading to human capital and democratic resilience in a technology-driven society._  
field: health-education-welfare · topic: — · school: — · format: interview · level: — · era: — · region: —  
speakers: James Marriott · discussed: —  
tags: civic engagement, cognitive skills, democracy, education, human capital, information technology, literacy, media consumption

**Incentives Are for Losers (with Adam Mastroianni)** — EconTalk · via EconTalk  
why: _Explores when incentives drive misconduct and how psychology reshapes standard economic assumptions._  
field: behavioral · topic: — · school: behavioral · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Russ Roberts, Adam Mastroianni · discussed: —  
tags: behavioral economics, dishonesty, incentives, misreporting, moral hazard, news media incentives, principal agent, selection effects

## topics frequency

inequality (13), ai-economy (11), interest-rates (7), china-economy (6), regulation (5), healthcare (5), tariffs (5), taxation (4), price-system (3), economic-growth (3), national-debt (3), gold-standard (2), socialism-vs-capitalism (2), housing (2), the-fed (2), great-depression (1), inflation (1), privatization (1), entrepreneurship (1), bitcoin (1), 2008-crisis (1)

## fields frequency

behavioral (15), history-of-thought (14), innovation (13), international (13), trade (12), labor (12), public (9), business (8), micro (7), macro (7), health-education-welfare (6), markets-investing (5), fiscal-macro (5), economic-history (4), law-econ (4), private-markets (4), business-cycles (3), development (3), urban-housing (3), money-bitcoin (3), environment-energy (3), intl-finance (2), monetary-policy (2), sound-money (2), credit (2), rates (2), general (2), finance (1), quantitative (1), alternatives (1), industrial-org (1), systems (1), macro-investing (1)

## schools frequency

classical-liberal (9), empirical (7), behavioral (7), public-choice (2), keynesian (1), new-institutional (1)

## format frequency

podcast-episode (121), interview (18), explainer (13), lecture (5), panel (2)

## level frequency

intermediate (88), introductory (9), expert (4)

## Tag vocabulary (932 distinct; ≥2 uses shown)

productivity (11), inequality (11), political economy (10), causal inference (6), behavioral economics (6), human capital (6), incentives (5), trade policy (5), public choice (5), regulatory capture (5), supply chains (5), economic growth (4), policy evaluation (4), rent seeking (4), free markets (4), public policy (4), corporate governance (4), sovereign debt (4), inequality measurement (4), market design (4), globalization (4), opportunity cost (3), labor supply (3), fiscal sustainability (3), tax policy (3), moral hazard (3), federal reserve (3), policy uncertainty (3), automation (3), intergenerational mobility (3), private equity (3), labor displacement (3), market power (3), labor markets (3), pricing (3), yield curve (3), interest rate risk (3), book review (3), classical liberalism (3), artificial intelligence (2), innovation policy (2), startup ecosystem (2), behavioral finance (2), risk management (2), market coordination (2), expectations (2), macroeconomic stabilization (2), monetary transmission (2), european integration (2), future of work (2), task automation (2), technological change (2), inflation dynamics (2), entrepreneurship (2), venture capital (2), cultural evolution (2), china shock (2), import competition (2), local labor markets (2), manufacturing employment (2), offshoring (2), trade adjustment (2), habit formation (2), self control (2), willpower (2), population aging (2), interest costs (2), public policy evaluation (2), democracy (2), fiscal policy (2), tax avoidance (2), wealth tax (2), monetary policy (2), evidence based economics (2), limited government (2), wealth inequality (2), organizational design (2), wage inequality (2), worker ownership (2), credit conditions (2), national debt (2), austerity (2), macroeconomic stagnation (2), living standards (2), family law (2), sanctions (2), ai adoption (2), economic policy (2), macroeconomic policy (2), antitrust (2), tariff policy (2), kalshi (2), prediction markets (2), banking union (2), income inequality (2), inflation expectations (2), capitalism (2), performance incentives (2), eurozone crisis (2), monetary fiscal interaction (2), policy tradeoffs (2), liberal democracy (2), income distribution (2), comparative advantage (2), financial literacy (2), household finance (2), retirement planning (2), consumer protection (2), matching markets (2), moral economics (2), assimilation (2), labor market effects (2), trade fragmentation (2), healthcare access (2), medical mistrust (2), representation (2), consumer price index (2), labor market statistics (2), measurement error (2), payment systems (2), stablecoins (2), hybrid work (2), remote work (2), work from home (2), workplace flexibility (2), evolutionary psychology (2), small business (2), consumer preferences (2), willingness to pay (2), product differentiation (2), consumer behavior (2), price signals (2), information asymmetry (2), innovation (2), cost effectiveness (2), inflation outlook (2), liquidity (2), book discussion (2), social norms (2), institutions (2), intellectuals (2), ideology (2), rule of law (2), social policy (2)

## Out-of-vocabulary values the model wanted (candidates for new topics)

- topics: {"v": "general", "c": 0.35} ×2
- topics: {"v": "general", "c": 0.3} ×2
- format: null ×2
- topics: {"v": "innovation", "c": 0.35} ×2
- topics: {"v": "general", "c": 0.55} ×2
- topics: {"v": "general", "c": 0.0} ×2
- topics: {"v": "general", "c": 0.25} ×2
- topics: {"v": "general", "c": 0.4} ×2
- fields: {"v": "education", "c": 0.78} ×1
- topics: {"v": "innovation", "c": 0.66} ×1
- topics: {"v": "general", "c": 0.2} ×1
- topics: {"v": "behavioral", "c": 0.55} ×1
- topics: {"v": "innovation", "c": 0.2} ×1
- topics: {"v": "environment-energy", "c": 0.65} ×1
- topics: {"v": "development", "c": 0.22} ×1
- topics: {"v": "transition", "c": 0.35} ×1
- regions: {"v": "spain", "c": 0.0} ×1
- topics: {"v": "economic-history", "c": 0.35} ×1
- topics: {"v": "social-contagion", "c": 0.7} ×1
- fields: {"v": "taxation", "c": 0.74} ×1
- fields: {"v": "education", "c": 0.0} ×1
- topics: {"v": "education", "c": 0.0} ×1
- fields: {"v": "political-economy", "c": 0.42} ×1
- regions: {"v": "france", "c": 0} ×1
- topics: {"v": "european-debt", "c": 0.0} ×1
- regions: {"v": "asia", "c": 0.55} ×1
- fields: {"v": "price-system", "c": 0.6} ×1
- topics: {"v": "general", "c": 0.6} ×1
- fields: {"v": "media", "c": 0.05} ×1
- topics: {"v": "innovation", "c": 0.05} ×1
- topics: {"v": "international", "c": 0.25} ×1
- topics: {"v": "economic-history", "c": 0.55} ×1
- topics: {"v": "development", "c": 0.25} ×1
