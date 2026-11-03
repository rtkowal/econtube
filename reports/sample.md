# Step 2 sample: classification report

Items in catalogue: 173; classified: 173.

## LLM usage this run

| model | step | calls | input tok | output tok |
|---|---|---:|---:|---:|
| gpt-5.4-nano | classify | 519 | 464,613 | 196,789 |
| gpt-5.4-nano | classify-retry | 303 | 270,514 | 114,980 |
| gpt-5.4-nano | gate | 148 | 37,312 | 4,592 |

Multiply by the model's current per-token price to get cost; per-item cost × expected catalogue size = backfill cost.

## Relevance gate

148 gated items, 131 rejected. Rejection reasons (first 25):

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
why: _Cowen and Tabarrok discuss AI’s economic implications, innovation incentives, and growth prospects._  
field: — · topic: — · school: — · format: interview · level: — · era: 2020s · region: —  
speakers: Tyler Cowen, Alex Tabarrok · discussed: —  
tags: artificial intelligence, economic growth, innovation incentives, productivity, science policy

**Francesco Sabella in Conversation With Victor Niederhoffer: Harvard Legend Hedge Fund Pioneer** — Francesco Sabella · via Marginal Revolution  
why: _A hedge-fund pioneer’s investing playbook, focused on markets, risk, and practical trading judgment._  
field: finance, markets-investing · topic: hedge-funds · school: — · format: interview · level: intermediate · era: — · region: —  
speakers: Francesco Sabella, Victor Niederhoffer · discussed: —  
tags: behavior under uncertainty, hedge fund strategy, market microstructure, risk management, trading discipline, value of markets

**2026, Methods Lecture, Melissa Dell and Ashesh Rambachan, "Estimation and Inference with AI...** — NBER · via Marginal Revolution  
why: _A rigorous lecture on econometric estimation and inference using modern AI-based methods._  
field: quantitative · topic: econometrics-and-causal-inference · school: — · format: lecture · level: expert · era: — · region: —  
speakers: Melissa Dell, Ashesh Rambachan · discussed: —  
tags: ai assisted methods, causal inference, cross fitting, econometric estimation, generalized estimators, machine learning, nber methods lecture

**A Price Is a Signal Wrapped Up in an Incentive** — Marginal Revolution University · via Marginal Revolution  
why: _Explains how prices convey information and shape behavior through incentives—core to market coordination._  
field: micro · topic: price-system · school: — · format: — · level: intermediate · era: timeless · region: —  
speakers: — · discussed: Friedrich Hayek, James M. Buchanan  
tags: buchanan, coordination problem, hayek, incentive design, market signals, price system, prices as information

**Was the China Shock Overblown? | Russ Roberts and Joseph Francis** — Hoover Institution · via Hoover Institution  
why: _Reassesses whether trade-driven Chinese import impacts on US jobs were overstated, with a focus on evidence._  
field: labor, international · topic: china-shock · school: — · format: podcast-episode · level: intermediate · era: — · region: china, us  
speakers: Russ Roberts, Joseph Francis · discussed: —  
tags: causal inference, china shock, empirical identification, import competition, labor market impacts, manufacturing jobs, trade adjustment

**The History of Macroeconomics from Keynes to HANK Models with Greg Kaplan** — Hoover Institution · via Hoover Institution  
why: _A guided history of modern macro modeling, from Keynes to HANK, with Nobel-era insights._  
field: history-of-thought, macro · topic: — · school: — · format: podcast-episode · level: intermediate · era: — · region: —  
speakers: Jon Hartley, Greg Kaplan · discussed: John Maynard Keynes, Robert E. Hall, Michael Woodford  
tags: hall, hank models, heterogeneous agent new keynesian, intertemporal optimization, keynesian economics, monetary policy transmission, new keynesian, nobel prize in economics, nominal rigidities, woodford

**Has China Become an Innovation Giant?** — Hoover Institution · via Hoover Institution  
why: _Investigates whether China’s innovation surge is real, measured, and driven by sustainable factors._  
field: innovation · topic: china-economy, economics-of-science · school: — · format: podcast-episode · level: intermediate · era: 2010s · region: china  
speakers: Josh Lerner, Amit Seru, Steven Davis · discussed: —  
tags: catch up vs frontier, china innovation, economics of science, industrial policy, patent data, r&d productivity, talent pipeline, technology diffusion

**The Billionaire Tax, The Busted Federal Budget, and the Future of the American Experiment** — Hoover Institution · via Hoover Institution  
why: _A clear fiscal-sustainability discussion linking budget politics, debt interest, and limits of tax-and-growth solutions._  
field: fiscal-macro · topic: national-debt, government-spending · school: — · format: — · level: — · era: — · region: us  
speakers: Joshua Rauh · discussed: —  
tags: billionaire tax, budget constraints, debt dynamics, federal budget, fiscal sustainability, inflation risk, interest costs, tax policy

**Taxing Billionaires, 9/11, and the Lessons We Forgot** — Hoover Institution · via Hoover Institution  
why: _Examines wealth-tax proposals and fiscal tradeoffs, alongside reflections on lessons after 9/11._  
field: fiscal-macro · topic: wealth-tax · school: — · format: podcast-episode · level: — · era: — · region: us  
speakers: — · discussed: —  
tags: 9/11, capital flight, fiscal policy, incentive effects, progressive taxation, public finances, tax incidence, wealth tax

**Make IPOs Great Again: SEC Chairman Paul Atkins on Ending Regulation by Enforcement** — Hoover Institution · via Hoover Institution  
why: _Discusses how IPO regulation affects capital formation and market dynamism from a pro-market enforcement-lite angle._  
field: — · topic: ipos-and-capital-markets, regulation · school: — · format: interview · level: intermediate · era: timeless · region: us  
speakers: Paul S. Atkins, Peter Robinson · discussed: —  
tags: capital formation, capital markets, ipo pipeline, market efficiency, regulation by enforcement, sec regulation, securities law

**Thomas Sowell on School Choice and the Price Our Children Pay for Bad Ideas | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Sowell applies evidence-based economics to school choice, arguing ideology harms students and outcomes._  
field: health-education-welfare · topic: education, school-choice · school: classical-liberal · format: lecture · level: intermediate · era: — · region: us  
speakers: Thomas Sowell · discussed: Charles Murray  
tags: affirmative action, education policy, ideology vs evidence, inequality of opportunity, resource allocation, school choice, standardized testing

**Teaching Gorbachev Capitalism: Powell, Rice, and Boskin Discuss George Shultz, the Economist** — Hoover Institution · via Hoover Institution  
why: _A high-profile discussion connecting Shultz’s economics to the Soviet transition and market reforms._  
field: — · topic: — · school: — · format: panel · level: — · era: — · region: —  
speakers: Jerome Powell, Condoleezza Rice, Michael Boskin · discussed: George P. Shultz, Mikhail Gorbachev  
tags: capitalism, cold war policy, gorbachev, institutional reform, market oriented reforms, shultz, transition economics

**Thomas Sowell: A Free Man | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Sowell’s life story tied to his ideas on liberty, incentives, and society’s economic outcomes._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: podcast-episode · level: intermediate · era: — · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: economic history, free markets, incentives, inequality, institutional analysis, poverty, public policy, skepticism of economic central planning

**Inflation Is A Choice: Kevin Warsh On Fixing The Federal Reserve | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Warsh critiques the Fed’s inflation management and outlines reforms to restore credibility._  
field: monetary-policy, macro · topic: inflation, the-fed · school: — · format: interview · level: intermediate · era: 2020s · region: us  
speakers: Kevin Warsh · discussed: —  
tags: central bank credibility, federal reserve, federal reserve chair nomination, inflation choice, monetary policy, policy regime, rate setting

**Thomas Sowell: Facts Against Rhetoric, Capitalism, Culture and Yes, the Tariffs | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Sowell challenges policy and cultural narratives using empirical arguments, including the case against tariffs._  
field: — · topic: — · school: — · format: interview · level: — · era: — · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: capitalism, comparative advantage, cultural explanations, economic incentives, facts vs rhetoric, inequality debates, tariff policy

**Thomas Sowell Discusses The Trump Tariffs | Uncommon Knowledge | Full Interview on April 15, 2025** — Hoover Institution · via Hoover Institution  
why: _A critical look at how tariffs affect prices, trade incentives, and overall economic welfare._  
field: — · topic: tariffs · school: — · format: interview · level: — · era: 2020s · region: —  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: comparative advantage, consumer costs, deadweight loss, protectionism, tariff incidence, trade policy, trump tariffs, uncommon knowledge

**Doing “The Best Things First,” with Bjorn Lomborg | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _A policymaker’s cost-benefit approach to choosing the most impactful actions on climate and development._  
field: — · topic: energy-and-climate · school: — · format: interview · level: — · era: — · region: —  
speakers: Bjorn Lomborg · discussed: —  
tags: climate policy, cost benefit analysis, prioritization, resource allocation, social welfare

**Consequences Matter: Thomas Sowell on “Social Justice Fallacies” | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques social-policy claims and argues that outcomes matter more than moral abstractions._  
field: — · topic: — · school: classical-liberal · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Thomas Sowell, Peter Robinson · discussed: —  
tags: government failure, inequality measurement, market outcomes, race and economics, social justice, unintended consequences, welfare policy

**The Ethos of Economics with John Cogan and Kevin Warsh** — Hoover Institution · via Hoover Institution  
why: _A thoughtful discussion on what economics should be and how to improve policy practice._  
field: history-of-thought · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: John Cogan, Kevin Warsh · discussed: —  
tags: coasean institutions, economic methodology, government effectiveness, incentives, institutional ethos, policy efficiency, public sector cost control, regulation

**Thomas Sowell on Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques expert-driven policymaking and connects ideas to real historical failures._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Franklin D. Roosevelt, members of FDR’s Brain Trust  
tags: expert failure, fdr brain trust, foresight bias, government decision making, institutional incentives, intellectuals, public policy, rule of law

**Thomas Sowell -- Basic Economics** — Hoover Institution · via Hoover Institution  
why: _A clear, policy-oriented primer on core economic reasoning from Thomas Sowell’s perspective._  
field: — · topic: — · school: classical-liberal · format: lecture · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: division of labor, incentives, knowledge problem, market coordination, opportunity cost, scarcity, social policy, trade offs

**Thomas Sowell on the second edition of Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _A broad discussion of how intellectuals shape social policy and the evidence behind competing narratives._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: interview · level: intermediate · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: comparative institutions, ideology, intellectuals and society, market vs state, social conflict, sowell

**Thomas Sowell -- Dismantling America** — Hoover Institution · via Hoover Institution  
why: _Thomas Sowell critiques American policy and ideas with sharp historical and economic reasoning._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell · discussed: —  
tags: free markets, inequality, intellectual history, public debate, social policy

**An Economist Looks at 90: Thomas Sowell on Charter Schools and Their Enemies** — Hoover Institution · via Hoover Institution  
why: _Thomas Sowell discusses charter schools, school choice, and policy critiques from a market-oriented perspective._  
field: health-education-welfare · topic: education, school-choice · school: classical-liberal · format: interview · level: — · era: — · region: us  
speakers: Thomas Sowell · discussed: —  
tags: charter schools, education policy, inequality, market competition, public vs private provision, school choice, us education reform

**Thomas Sowell and a Conflict of Visions** — Hoover Institution · via Hoover Institution  
why: _Sowell contrasts visions and interests to explain recurring political conflict and policy disagreements._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: classical liberalism, cognitive framing, ideas and institutions, political economy, visions vs interests

**Facts and Fallacies with Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _A clear, argument-driven debunking of popular myths about economics and social outcomes._  
field: — · topic: — · school: classical-liberal · format: — · level: intermediate · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: economic inequality, human capital, market incentives, misconceptions in economics, policy evaluation, race and economics, welfare programs

**Thomas Sowell discusses his newest book, Intellectuals and Race** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques how intellectual movements shape race-related debates and broader social outcomes._  
field: history-of-thought · topic: — · school: — · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: —  
tags: book discussion, education, inequality, intellectuals, policy debates, race and society, social movements

**Thomas Sowell on the Housing Boom and Bust** — Hoover Institution · via Hoover Institution  
why: _Explains how politics and incentives fueled the housing bubble and the 2008 bust._  
field: — · topic: housing, 2008-crisis · school: — · format: — · level: expert · era: 2008-crisis, 2000s · region: us  
speakers: Thomas Sowell · discussed: —  
tags: 2008 crisis, asset bubble, credit cycle, government policy, housing boom, housing bust, political incentives, subprime mortgage

**Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _A thought-provoking Sowell interview on inequality, ideas in economics, and public policy debates._  
field: history-of-thought · topic: — · school: classical-liberal · format: interview · level: — · era: timeless · region: —  
speakers: Thomas Sowell, Peter Robinson · discussed: Barack Obama  
tags: barack obama, class warfare, economic inequality, limited government, public policy, the thomas sowell reader

**Wealth, Poverty, and Politics** — Hoover Institution · via Hoover Institution  
why: _Thomas Sowell compares global and U.S. poverty and argues about the politics behind policy choices._  
field: development · topic: poverty · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell · discussed: —  
tags: cross country comparison, human capital, income inequality, political economy, poverty, welfare policy

**Richard Epstein Enriches Us with His Ideas on Inequality, Taxes, Politics, and Health Care** — Hoover Institution · via Hoover Institution  
why: _A sharp law-and-economics take on taxes, inequality, and health care within a free-market framework._  
field: law-econ · topic: inequality, taxation · school: classical-liberal · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Richard A. Epstein · discussed: —  
tags: constitutional political economy, free markets, gay marriage, globalization, health care reform, inequality, property rights, tax policy

**First reactions | Michael Woodford, prize in economic sciences 2026 | Telephone interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _A quick Nobel callback with Michael Woodford on his initial reactions and context for the prize._  
field: history-of-thought · topic: history-of-economic-thought · school: — · format: interview · level: — · era: timeless · region: —  
speakers: Michael Woodford · discussed: —  
tags: autumn exam, central banking, economic sciences, macroeconomic policy, telephone interview

**Announcement of the 2026 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Concise announcement highlighting Hall and Woodford’s influential work linking micro foundations to stabilization policy._  
field: — · topic: — · school: — · format: — · level: — · era: timeless · region: global  
speakers: — · discussed: Robert E. Hall, Michael Woodford  
tags: alfred nobel, inflation, macroeconomic stabilization, microeconomic foundations, monetary policy, rational expectations, riksbank prize

**“One of the biggest policy questions we have in macroeconomics.” | 2026 economic sciences interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Explains a key macro question on modeling business cycles and evaluating stabilization policy._  
field: macro, business-cycles · topic: business-cycle · school: — · format: interview · level: — · era: — · region: —  
speakers: Timo Boppart, Owen Gaffney · discussed: —  
tags: business cycle, economic sciences interview, macroeconomic framework, policy evaluation, stabilization policy

**Roman Mars on Flags, Phones, and the Design of Everyday Life** — Conversations with Tyler · via Conversations with Tyler  
why: _A fascinating design lens on how small features shape behavior in everyday urban life._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Roman Mars, Tim Harford · discussed: —  
tags: behavioral design, choice architecture, cognitive biases, design systems, everyday objects, urban design, wayfinding

**Liaquat Ahamed on Financial Crises, Gold, and the Lessons of 1873** — Conversations with Tyler · via Conversations with Tyler  
why: _Explains 1873’s crisis through gold and finance networks, drawing lessons for later depressions._  
field: economic-history · topic: gold-standard, economic-history-of-europe · school: — · format: podcast-episode · level: intermediate · era: pre-1900 · region: —  
speakers: Liaquat Ahamed · discussed: Tyler Cowen  
tags: 1873 panic, bretton woods, central banking, financial crises, financial history, gold standard, international finance, lenders of last resort

**Luis Garicano on Spain, Europe, and the Future of Work** — Conversations with Tyler · via Conversations with Tyler  
why: _Garicano connects Spain and Europe’s institutions to how technology reshapes jobs and inequality._  
field: labor · topic: — · school: — · format: podcast-episode · level: intermediate · era: — · region: spain  
speakers: Luis Garicano · discussed: Gary Becker, Kevin Murphy, Sherwin Rosen  
tags: automation, europes economic model, future of work, labor markets, productivity, structural reforms, technological change

**Gita Gopinath on Trade, Currencies, and Economic Transformation** — Conversations with Tyler · via Conversations with Tyler  
why: _A high-level discussion of how currencies, trade, and global institutions shape economic transformation._  
field: international, intl-finance · topic: exchange-rates · school: — · format: podcast-episode · level: intermediate · era: — · region: global  
speakers: Gita Gopinath, Tyler Cowen · discussed: —  
tags: economic transformation, exchange rate regimes, imf, inflation, international monetary system, sovereign debt restructuring, trade policy

**Annie Lowrey on the Time Tax, Fraud, and Rationing by Paperwork** — Conversations with Tyler · via Conversations with Tyler  
why: _Explores how paperwork and administrative friction function like a regressive tax on the poor._  
field: public · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: us  
speakers: Annie Lowrey · discussed: Tyler Cowen  
tags: administrative costs, forms and compliance, fraud incentives, paperwork burdens, rationing by bureaucracy, regressive levies, time tax, us bureaucracy, welfare access

**Jared Diamond on Leaders, Luck, and Irreplaceability** — Conversations with Tyler · via Conversations with Tyler  
why: _A compelling debate on whether leaders drive history or whether luck and constraints dominate outcomes._  
field: — · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Jared Diamond, Tyler Cowen · discussed: —  
tags: contingency, genghis khan, historical causation, irreplaceability, leadership, luck vs agency, prophets, roman empire

**Michael Moritz on Origin Stories, Exile, and Obsessive Curiosity** — Conversations with Tyler · via Conversations with Tyler  
why: _A business-and-innovation memoir conversation connecting personal exile with company-building stories._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Michael Moritz, Tyler Cowen · discussed: —  
tags: alex ferguson, apple history, chrysler turnaround, exile and identity, journalism, manchester united, origin stories, sequoia capital, venture capital

**Luke Burgis on Mimetic Desire, Catholicism, and the Age of Social Contagion** — Conversations with Tyler · via Conversations with Tyler  
why: _An engaging interview using Girard’s ideas to interpret desire, belief, and societal spread._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Luke Burgis, Tyler · discussed: René Girard  
tags: catholicism, cluny institute, mimetic desire, priesthood, religion and society, rené girard, social contagion

**Revisiting the China Shock (with Joseph Francis)** — EconTalk · via EconTalk  
why: _Reassesses whether the China-shock job narrative holds using scrutiny of influential evidence._  
field: trade · topic: china-shock, labor-markets · school: — · format: podcast-episode · level: intermediate · era: 2000s · region: china, us  
speakers: Joseph Francis · discussed: David Autor, Daron Acemoglu, Gordon Hanson  
tags: causal inference, china shock, import competition, job displacement, local labor markets, manufacturing decline, paper replication, trade liberalization

**How Your Situation Shapes You (with Angela Duckworth)** — EconTalk · via EconTalk  
why: _Links behavioral economics to practical habit change: environments and relationships shape outcomes._  
field: behavioral · topic: behavioral-economics · school: behavioral · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Angela Duckworth, Russ Roberts · discussed: —  
tags: behavioral change, choice architecture, grit, habits, self control, social environment, willpower

**Lives Wasted and Well-Lived: David Wolpe on The Death of Ivan Ilyich** — EconTalk · via EconTalk  
why: _A reflective literature-and-life conversation that probes how people evaluate choices near death._  
field: — · topic: — · school: — · format: interview · level: — · era: — · region: —  
speakers: Russ Roberts, David Wolpe · discussed: —  
tags: ivam ilyich, meaning of life, moral philosophy, mortality, tolstoy

**The Great Fertility Collapse (with Jesus Fernandez-Villaverde)** — EconTalk · via EconTalk  
why: _Explores why fertility is falling worldwide and what it implies for growth, labor markets, and policy._  
field: development · topic: — · school: — · format: podcast-episode · level: — · era: — · region: global  
speakers: Jesus Fernandez-Villaverde · discussed: —  
tags: demographics, dependency ratios, economic development, fertility decline, human capital, intergenerational transfers, labor supply, population aging

**Addiction, Faith, and the Limits of Willpower (with Meghan O'Gieblyn)** — EconTalk · via EconTalk  
why: _Explores addiction through behavioral lenses, challenging willpower-first explanations._  
field: behavioral · topic: behavioral-economics · school: behavioral · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Meghan O'Gieblyn · discussed: —  
tags: addiction, behavioral decision making, faith and motivation, habit formation, iris murdoch, limited willpower, psychology of choice, self control, simone weil, william james

**Public Choice and Politics Without Romance (with Mike Munger)** — EconTalk · via EconTalk  
why: _Applies public-choice logic to political incentives, skepticism, and limits on government power._  
field: law-econ · topic: public-choice-government-failure · school: public-choice · format: podcast-episode · level: intermediate · era: — · region: —  
speakers: Russ Roberts, Mike Munger · discussed: James M. Buchanan, Gordon Tullock  
tags: bureaucracy, constitutional political economy, government failure, median voter theorem, political incentives, public choice, rent seeking

**The Death of Reading (with James Marriott)** — EconTalk · via EconTalk  
why: _Explores how declining reading threatens democratic accountability and social outcomes._  
field: — · topic: education · school: — · format: podcast-episode · level: — · era: timeless · region: —  
speakers: James Marriott, Russ Roberts · discussed: —  
tags: cognitive skills, democracy, education policy, information ecosystems, literacy, media consumption

**Incentives Are for Losers (with Adam Mastroianni)** — EconTalk · via EconTalk  
why: _Explores when incentives drive socially harmful behavior and how psychology reframes “rational” compliance._  
field: behavioral · topic: behavioral-economics · school: — · format: podcast-episode · level: — · era: — · region: —  
speakers: Russ Roberts, Adam Mastroianni · discussed: —  
tags: behavioral economics, bounded rationality, cheating and compliance, ethical behavior, goal displacement, incentives, moral hazard, principal agent problems

## topics frequency

history-of-economic-thought (8), behavioral-economics (8), ai-economy (8), education (6), inequality (5), labor-markets (4), regulation (4), tariffs (4), healthcare (4), china-shock (3), china-economy (3), economics-of-science (3), globalization (3), bonds-and-yields (3), econometrics-and-causal-inference (2), gold-standard (2), business-cycle (2), national-debt (2), wealth-tax (2), ipos-and-capital-markets (2), school-choice (2), austerity (2), sanctions-and-economic-statecraft (2), housing (2), immigration (2), stablecoins (2), energy-and-climate (2), credit-markets (2), hedge-funds (1), price-system (1), economic-history-of-europe (1), exchange-rates (1), government-spending (1), public-choice-government-failure (1), dollar-dominance (1), private-equity (1), antitrust (1), zoning-and-land-use (1), industrial-policy (1), inflation (1), the-fed (1), development-and-poverty-traps (1), interest-rates (1), bitcoin (1), 2008-crisis (1), poverty (1), taxation (1), rule-of-law (1)

## fields frequency

history-of-thought (13), international (11), innovation (10), behavioral (10), labor (9), trade (7), law-econ (7), health-education-welfare (7), fiscal-macro (6), macro (5), development (4), business (4), markets-investing (3), public (3), money-bitcoin (3), quantitative (2), micro (2), economic-history (2), business-cycles (2), intl-finance (2), private-markets (2), general (2), environment-energy (2), rates (2), credit (2), finance (1), industrial-org (1), urban-housing (1), monetary-policy (1), macro-investing (1), sound-money (1)

## schools frequency

classical-liberal (7), empirical (3), behavioral (2), public-choice (1)

## format frequency

podcast-episode (127), interview (15), explainer (12), lecture (3), panel (1)

## level frequency

intermediate (67), introductory (8), expert (3)

## Tag vocabulary (936 distinct; ≥2 uses shown)

inequality (19), productivity (9), political economy (9), incentives (8), human capital (7), causal inference (6), book review (6), automation (5), trade policy (5), government failure (4), public choice (4), rent seeking (4), behavioral economics (4), fiscal policy (4), free markets (4), public policy (4), supply chains (4), book discussion (4), pricing (4), risk management (3), inflation (3), monetary policy (3), labor market impacts (3), economics of science (3), tax policy (3), education policy (3), innovation (3), labor displacement (3), wealth inequality (3), economic statecraft (3), sovereign debt (3), institutional design (3), property rights (3), economic methodology (3), economic inequality (3), comparative advantage (3), behavioral biases (3), evolutionary psychology (3), market incentives (3), intellectual history (3), artificial intelligence (2), innovation incentives (2), choice architecture (2), central banking (2), rational expectations (2), business cycle (2), policy evaluation (2), structural reforms (2), china shock (2), import competition (2), job displacement (2), industrial policy (2), behavioral change (2), self control (2), demographics (2), labor supply (2), billionaire tax (2), budget constraints (2), fiscal sustainability (2), habit formation (2), constitutional political economy (2), political incentives (2), capital flight (2), progressive taxation (2), wealth tax (2), capital markets (2), market efficiency (2), inequality of opportunity (2), resource allocation (2), school choice (2), capitalism (2), institutional analysis (2), poverty (2), sovereign risk (2), labor market adjustment (2), labor bargaining (2), austerity (2), private equity (2), income inequality (2), family law (2), ai adoption (2), lobbying (2), eurozone governance (2), macroeconomic instability (2), market power (2), regulatory capture (2), geopolitical risk (2), prediction markets (2), securities regulation (2), eurozone (2), germany (2), inflation expectations (2), market vs state (2), central bank credibility (2), federal reserve (2), bond markets (2), european economy (2), protectionism (2), consumer decision making (2), debt management (2), financial literacy (2), household finance (2), numeracy (2), retirement planning (2), matching markets (2), moral economics (2), assimilation (2), evidence based policy (2), immigration myths (2), globalization (2), medical mistrust (2), representation (2), data quality (2), labor statistics (2), remote work (2), work from home (2), institutional development (2), product differentiation (2), information asymmetry (2), risk premium (2), r&d (2), opportunity cost (2), institutional incentives (2), communication (2), inequality measurement (2), credit underwriting (2), classical liberalism (2), duration (2), race and economics (2), welfare policy (2), education (2), intellectuals (2), rule of law (2), social policy (2)

## Out-of-vocabulary values the model wanted (candidates for new topics)

- topics: {"v": "general", "c": 0.0} ×3
- topics: {"v": "general", "c": 0.35} ×2
- topics: {"v": "general", "c": 0.3} ×2
- format: null ×2
- topics: {"v": "innovation", "c": 0.35} ×2
- topics: {"v": "general", "c": 0.55} ×2
- topics: {"v": "economic-history", "c": 0.35} ×2
- topics: {"v": "general", "c": 0.25} ×2
- topics: {"v": "general", "c": 0.4} ×2
- topics: {"v": "development", "c": 0.25} ×2
- fields: {"v": "education", "c": 0.78} ×1
- topics: {"v": "innovation", "c": 0.66} ×1
- topics: {"v": "general", "c": 0.2} ×1
- topics: {"v": "behavioral", "c": 0.55} ×1
- topics: {"v": "innovation", "c": 0.2} ×1
- topics: {"v": "environment-energy", "c": 0.65} ×1
- topics: {"v": "development", "c": 0.22} ×1
- topics: {"v": "transition", "c": 0.35} ×1
- regions: {"v": "spain", "c": 0.0} ×1
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
- topics: {"v": "history-of-thought", "c": 0.72} ×1
- topics: {"v": "general", "c": 0.28} ×1
- regions: {"v": "europe", "c": 0.25} ×1
- topics: {"v": "trade", "c": 0.55} ×1
- topics: {"v": "competition", "c": 0.6} ×1
- topics: {"v": "business", "c": 0.25} ×1
- topics: {"v": "general", "c": 0.45} ×1
- topics: {"v": "health-education-welfare", "c": 0.3} ×1
- topics: {"v": "credit", "c": 0.05} ×1
- fields: {"v": "competition", "c": 0.0} ×1
- regions: {"v": "europe", "c": 0.75} ×1
- fields: {"v": "housing", "c": 0.95} ×1
- topics: {"v": "trade", "c": 0.74} ×1
- topics: {"v": "monetary-policy", "c": 0.25} ×1
- fields: {"v": "money", "c": 0.15} ×1
- topics: {"v": "trust", "c": 0.25} ×1
- fields: {"v": "taxation", "c": 0.28} ×1
- regions: {"v": "europ zone", "c": 0.0} ×1
- topics: {"v": "history-of-thought", "c": 0.28} ×1
- fields: {"v": "inequality", "c": 0.9} ×1
- topics: {"v": "incentives", "c": 0.0} ×1
- topics: {"v": "labor", "c": 0.2} ×1
- topics: {"v": "health-education-welfare", "c": 0.35} ×1
- topics: {"v": "private-markets", "c": 0.15} ×1
- fields: {"v": "political-economy", "c": 0.62} ×1
- topics: {"v": "social-contract", "c": 0.52} ×1
- eras: {"v": "1900s-2000s", "c": 0.6} ×1
