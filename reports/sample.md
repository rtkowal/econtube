# Step 2 sample: classification report

Items in catalogue: 173; classified: 173.

## LLM usage this run

| model | step | calls | input tok | output tok |
|---|---|---:|---:|---:|
| gpt-5.4-nano | classify | 173 | 130,997 | 67,570 |
| gpt-5.4-nano | classify-retry | 164 | 136,284 | 63,341 |
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
why: _A smart discussion on AI’s economic impact and how incentives shape innovation and growth._  
field: innovation · topic: ai-economy · school: — · format: — · level: — · era: 2020s · region: —  
speakers: Tyler Cowen, Alex Tabarrok, Wyatt Thompson · discussed: Tyler Cowen, Alex Tabarrok  
tags: ai, economic-growth, future-of-work, innovation, marginal-revolution, openai, productivity, technology-policy

**Francesco Sabella in Conversation With Victor Niederhoffer: Harvard Legend Hedge Fund Pioneer** — Francesco Sabella · via Marginal Revolution  
why: _Hedge-fund pioneer Niederhoffer discusses how markets behave and how to manage trading risk._  
field: markets-investing, finance · topic: — · school: — · format: — · level: — · era: — · region: us  
speakers: Francesco Sabella, Victor Niederhoffer · discussed: Francesco Sabella, Victor Niederhoffer  
tags: alternative investments, hedge funds, market timing, risk management, trading

**2026, Methods Lecture, Melissa Dell and Ashesh Rambachan, "Estimation and Inference with AI...** — NBER · via Marginal Revolution  
why: _Practical methods for using AI in econometric estimation and inference, with rigorous inference guidance._  
field: innovation, quantitative · topic: ai-economy · school: — · format: — · level: expert · era: 2020s · region: —  
speakers: Melissa Dell, Ashesh Rambachan · discussed: Melissa Dell, Ashesh Rambachan  
tags: causal inference, econometrics, estimation, inference with ai, machine learning, nber

**A Price Is a Signal Wrapped Up in an Incentive** — Marginal Revolution University · via Marginal Revolution  
why: _Explains how prices convey information and shape incentives to coordinate economic decisions._  
field: micro · topic: price-system · school: — · format: — · level: — · era: timeless · region: —  
speakers: — · discussed: —  
tags: incentives, information problem, marginal incentives, market coordination, price signals

**Was the China Shock Overblown? | Russ Roberts and Joseph Francis** — Hoover Institution · via Hoover Institution  
why: _Evaluates whether the China shock story overstates job losses and how to interpret the evidence._  
field: trade, labor · topic: china-economy · school: — · format: — · level: intermediate · era: — · region: china, us  
speakers: Russ Roberts, Joseph Francis · discussed: —  
tags: causal inference, china shock, hoover institution, import competition, labor-market impacts, local labor markets, manufacturing employment, trade adjustment

**The History of Macroeconomics from Keynes to HANK Models with Greg Kaplan** — Hoover Institution · via Hoover Institution  
why: _A clear tour from Keynesian macro to HANK models, highlighting Kaplan’s contributions and the Woodford-Hall Nobel work._  
field: macro · topic: — · school: keynesian · format: podcast-episode · level: intermediate · era: — · region: global  
speakers: Gregory Kaplan, Jon Hartley · discussed: John Maynard Keynes, Robert Hall, Michael Woodford, Gregory Kaplan  
tags: consumption inequality, hank, heterogeneous-agent models, hoover institution, microfoundations, monetary policy transmission, new keynesian

**Has China Become an Innovation Giant?** — Hoover Institution · via Hoover Institution  
why: _Evaluates whether China’s innovation surge is real, measurable, and driven by underlying talent and incentives._  
field: innovation · topic: economic-growth · school: — · format: — · level: intermediate · era: — · region: china  
speakers: Josh Lerner, Amit Seru, Steven Davis · discussed: Josh Lerner, Amit Seru, Steven Davis  
tags: china innovation, industrial research, innovation measurement, institutional incentives, r&d productivity, science policy, technology adoption

**The Billionaire Tax, The Busted Federal Budget, and the Future of the American Experiment** — Hoover Institution · via Hoover Institution  
why: _A clear policy-focused discussion of why debt dynamics can overwhelm tax and growth plans._  
field: fiscal-macro · topic: national-debt · school: — · format: — · level: intermediate · era: — · region: us  
speakers: Joshua Rauh · discussed: Joshua Rauh  
tags: billionaire tax, budget constraints, federal debt, fiscal sustainability, inflation risk, interest costs, spending control, tax policy

**Taxing Billionaires, 9/11, and the Lessons We Forgot** — Hoover Institution · via Hoover Institution  
why: _Analyzes billionaire wealth taxes and links post-9/11 lessons to today’s fiscal choices._  
field: fiscal-macro · topic: taxation · school: — · format: — · level: — · era: 2020s · region: us  
speakers: — · discussed: —  
tags: 9/11, economic incentives, fiscal policy, inequality, progressive taxation, tax compliance, wealth tax

**Make IPOs Great Again: SEC Chairman Paul Atkins on Ending Regulation by Enforcement** — Hoover Institution · via Hoover Institution  
why: _Discusses how securities enforcement and regulation affect IPO incentives and capital formation._  
field: equities, law-econ · topic: regulation · school: — · format: — · level: — · era: — · region: us  
speakers: Paul Atkins, Peter Robinson · discussed: Paul Atkins, Peter Robinson  
tags: capital formation, capital markets, hoover institution, ipo market, regulation by enforcement, sec enforcement, securities regulation

**Thomas Sowell on School Choice and the Price Our Children Pay for Bad Ideas | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _A data-driven critique of education policy and school choice, including affirmative action and university failures._  
field: health-education-welfare · topic: inequality · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: affirmative action, education policy, higher education, ideology vs evidence, inequality, school choice

**Teaching Gorbachev Capitalism: Powell, Rice, and Boskin Discuss George Shultz, the Economist** — Hoover Institution · via Hoover Institution  
why: _Policy heavy discussion of Shultz’s economic thinking and lessons for capitalism and reform._  
field: monetary-policy · topic: the-fed · school: — · format: — · level: — · era: — · region: us  
speakers: Jerome H. Powell, Condoleezza Rice, Michael J. Boskin · discussed: George P. Shultz, Mikhail Gorbachev  
tags: cold war legacy, economic policy, federal reserve, inflation, market reforms, monetary policy, shultz

**Thomas Sowell: A Free Man | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Sowell’s own life story and economics perspective on freedom, institutions, and social outcomes._  
field: history-of-thought · topic: socialism-vs-capitalism · school: classical-liberal · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Thomas Sowell  
tags: civil society, cultural and institutional explanations, free markets, government limits, incentives, inequality

**Inflation Is A Choice: Kevin Warsh On Fixing The Federal Reserve | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Kevin Warsh critiques Fed policy and outlines reforms for restoring stable inflation and credibility._  
field: monetary-policy, macro, rates · topic: inflation, the-fed · school: — · format: — · level: — · era: 2020s · region: us  
speakers: Kevin Warsh · discussed: Donald Trump, Federal Reserve (Fed)  
tags: central bank independence, federal reserve, hoover institution, inflation targeting, interest-rate policy, monetary policy framework

**Thomas Sowell: Facts Against Rhetoric, Capitalism, Culture and Yes, the Tariffs | Hoover Institution** — Hoover Institution · via Hoover Institution  
why: _Sowell and Robinson discuss how empirical facts challenge popular political rhetoric, including arguments against tariffs._  
field: history-of-thought · topic: tariffs · school: classical-liberal · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell, Peter Robinson · discussed: Thomas Sowell, Peter Robinson  
tags: capitalism, culture, facts-against-rhetoric, free trade, hoover-institution, institutional criticism, tariffs

**Thomas Sowell Discusses The Trump Tariffs | Uncommon Knowledge | Full Interview on April 15, 2025** — Hoover Institution · via Hoover Institution  
why: _Sowell critiques new Trump tariffs, arguing their economic impacts on prices and incentives._  
field: trade · topic: tariffs · school: — · format: — · level: — · era: 2020s · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Donald Trump  
tags: consumer costs, economic incentives, hoover institution, protectionism, supply chains, tariffs, trade policy

**Doing “The Best Things First,” with Bjorn Lomborg | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Applies cost-benefit reasoning to choose which social problems to tackle first, grounded in evidence._  
field: environment-energy · topic: — · school: — · format: — · level: — · era: — · region: —  
speakers: Bjorn Lomborg · discussed: Bjorn Lomborg  
tags: copenhagen consensus center, cost-benefit analysis, evidence-based policy, global challenges, policy evaluation, priority setting

**Consequences Matter: Thomas Sowell on “Social Justice Fallacies” | Uncommon Knowledge** — Hoover Institution · via Hoover Institution  
why: _Sharp critique of social-justice arguments grounded in incentives, evidence, and unintended consequences._  
field: public · topic: — · school: classical-liberal · format: — · level: intermediate · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Thomas Sowell, Peter Robinson  
tags: bureaucratic incentives, civil society, distributional effects, market incentives, policy evaluation, rights vs outcomes, social justice

**The Ethos of Economics with John Cogan and Kevin Warsh** — Hoover Institution · via Hoover Institution  
why: _Two policy veterans discuss how economics should guide government decisions and institutional design._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: — · region: us  
speakers: John Cogan, Kevin Warsh · discussed: John Cogan, Kevin Warsh  
tags: economics-ethos, government-cost-control, institutional-design, intellectual-standards, policy-efficiency

**Thomas Sowell on Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _Sowell explains how elite expertise can misfire in policymaking, using historical examples and critiques._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Franklin D. Roosevelt  
tags: brain trust, expertise, hoover institution, institutional critique, intellectuals, knowledge problem, policy failure

**Thomas Sowell -- Basic Economics** — Hoover Institution · via Hoover Institution  
why: _A clear, foundational walkthrough of core economics principles from a well-known critic of bad economic reasoning._  
field: general · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: economic incentives, intellectual history, marginal analysis, markets, opportunity cost, scarcity, supply and demand

**Thomas Sowell on the second edition of Intellectuals and Society** — Hoover Institution · via Hoover Institution  
why: _A wide-ranging interview on how intellectuals shape policy debates and why outcomes diverge from ideals._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: cultural-conflict, intellectuals-and-society, knowledge-and-ideology, market-economics, public-intellectuals, social-policy

**Thomas Sowell -- Dismantling America** — Hoover Institution · via Hoover Institution  
why: _A Thomas Sowell talk connecting economic ideas to policy debates about America’s direction._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: hoover institution, inequality, intellectual history, public policy, rights and institutions, socialism vs capitalism

**An Economist Looks at 90: Thomas Sowell on Charter Schools and Their Enemies** — Hoover Institution · via Hoover Institution  
why: _Sowell discusses charter schools and policy opposition with a sharp, evidence-focused lens on education._  
field: health-education-welfare · topic: — · school: — · format: — · level: — · era: 2020s · region: us  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: charter schools, education policy, inequality of opportunity, public vs private provision, regulation, school choice

**Thomas Sowell and a Conflict of Visions** — Hoover Institution · via Hoover Institution  
why: _Explains how competing visions shape political debate and policy outcomes, beyond stated interests._  
field: public · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: classical liberalism, hoover institution, ideology, interests vs visions, political assumptions, public policy

**Facts and Fallacies with Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _Sowell challenges popular myths about economics and social outcomes with sharp, evidence-focused reasoning._  
field: history-of-thought · topic: inequality · school: — · format: — · level: — · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: bias-vs-data, critical-thinking, economic-misconceptions, inequality, policy-debates, race-and-economics

**Thomas Sowell discusses his newest book, Intellectuals and Race** — Hoover Institution · via Hoover Institution  
why: _Sowell explains how elite ideas shape racial and societal outcomes, with historical perspective._  
field: history-of-thought · topic: — · school: — · format: podcast-episode · level: intermediate · era: timeless · region: —  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: hoover institution, ideology, inequality, intellectuals, public intellectuals, race

**Thomas Sowell on the Housing Boom and Bust** — Hoover Institution · via Hoover Institution  
why: _Explains how housing policy and incentives helped fuel the boom and crash into 2008._  
field: urban-housing · topic: 2008-crisis, housing · school: — · format: — · level: — · era: 2008-crisis, 2000s · region: us  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: credit misallocation, financial crisis, government policy, housing boom, housing bust, mortgage securitization, subprime mortgages

**Thomas Sowell** — Hoover Institution · via Hoover Institution  
why: _An engaging interview on ideas in public policy, inequality debates, and Sowell’s perspectives._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell, Peter Robinson · discussed: Barack Obama  
tags: class warfare, hoover institution, inequality, obama politics, public policy, thomas sowell reader

**Wealth, Poverty, and Politics** — Hoover Institution · via Hoover Institution  
why: _A clear, policy-relevant discussion comparing U.S. and global poverty and how politics shapes perceptions._  
field: — · topic: inequality · school: — · format: — · level: — · era: timeless · region: us  
speakers: Thomas Sowell · discussed: Thomas Sowell  
tags: income inequality, living standards, politics and poverty, poverty measurement, welfare policy, world poverty comparison

**Richard Epstein Enriches Us with His Ideas on Inequality, Taxes, Politics, and Health Care** — Hoover Institution · via Hoover Institution  
why: _A clear policy-focused discussion of inequality, taxes, and healthcare from a libertarian legal-economics perspective._  
field: law-econ · topic: inequality, taxation · school: classical-liberal · format: interview · level: intermediate · era: timeless · region: —  
speakers: Richard A. Epstein · discussed: Richard A. Epstein  
tags: free markets, globalization, healthcare reform, hoover institution, inequality, property rights, tax policy

**First reactions | Michael Woodford, prize in economic sciences 2026 | Telephone interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Quick Nobel Prize reaction interview offering insight into a leading economist’s thinking._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Michael Woodford · discussed: Michael Woodford  
tags: academic-economics, economic-sciences, nobel-prize, stockholm, telephone-interview

**Announcement of the 2026 Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Prize announcement highlighting microfoundations for macro stabilization—key ideas for modern monetary policy._  
field: macro, micro · topic: — · school: — · format: — · level: — · era: timeless · region: global  
speakers: Robert E. Hall, Michael Woodford · discussed: Robert E. Hall, Michael Woodford  
tags: macroeconomic-stabilisation, microfoundations, monetary-policy, new-keynesian-macro, riksbank-prize

**“One of the biggest policy questions we have in macroeconomics.” | 2026 economic sciences interview** — Nobel Prize · via Nobel Prize - Economic Sciences  
why: _Nobel committee interview explains how new frameworks improve analysis of business cycles and stabilization policy._  
field: macro, business-cycles · topic: — · school: — · format: — · level: — · era: — · region: —  
speakers: Timo Boppart, Owen Gaffney · discussed: Timo Boppart  
tags: business cycles, economic sciences nobel prize, macroeconomic framework, policy evaluation, stabilisation policy

**Roman Mars on Flags, Phones, and the Design of Everyday Life** — Conversations with Tyler · via Conversations with Tyler  
why: _A design-focused conversation showing how everyday symbols and interfaces shape behavior and city life._  
field: innovation · topic: — · school: — · format: — · level: — · era: timeless · region: —  
speakers: Roman Mars, Tyler Cowen · discussed: Roman Mars  
tags: behavioral cues, design of everyday life, graphic design, human-computer interaction, public space, urban design, wayfinding

**Liaquat Ahamed on Financial Crises, Gold, and the Lessons of 1873** — Conversations with Tyler · via Conversations with Tyler  
why: _Ahamed explains the 1873 crisis and gold-era finance, drawing lessons from earlier banking breakdowns._  
field: economic-history · topic: gold-standard · school: — · format: — · level: — · era: pre-1900 · region: global  
speakers: Liaquat Ahamed, Tyler Cowen · discussed: Liaquat Ahamed, Tyler Cowen, Rothschilds  
tags: 1870s depression, 1873 panic, credit contraction, financial crises, gold standard, international finance, rothschild family

**Luis Garicano on Spain, Europe, and the Future of Work** — Conversations with Tyler · via Conversations with Tyler  
why: _Garicano connects European labor realities to tech-driven change and institutions shaping work._  
field: labor · topic: — · school: — · format: — · level: — · era: — · region: eurozone  
speakers: Luis Garicano, Tyler Cowen · discussed: Luis Garicano, Tyler Cowen, Gary Becker, Kevin Murphy, Sherwin Rosen  
tags: automation, europe, european-parliament, future-of-work, institutional-design, labor-markets, productivity, skills, spain

**Gita Gopinath on Trade, Currencies, and Economic Transformation** — Conversations with Tyler · via Conversations with Tyler  
why: _IMF insider perspective on currencies, trade, and how economies transform under shifting global conditions._  
field: international, macro, intl-finance · topic: — · school: — · format: — · level: — · era: — · region: global  
speakers: Gita Gopinath, Tyler Cowen · discussed: Gita Gopinath  
tags: capital flows, disinflation, exchange rates, imf, macroeconomic transformation, sovereign debt restructuring, trade policy

**Annie Lowrey on the Time Tax, Fraud, and Rationing by Paperwork** — Conversations with Tyler · via Conversations with Tyler  
why: _A sharp discussion of how paperwork burdens act like a regressive tax, especially harming the poor._  
field: public · topic: inequality · school: — · format: — · level: intermediate · era: timeless · region: us  
speakers: Annie Lowrey, Tyler Cowen · discussed: Annie Lowrey, Tyler Cowen  
tags: bureaucratic inefficiency, fraud and compliance incentives, paperwork costs, rationing by administration, regressive policy design, time poverty

**Jared Diamond on Leaders, Luck, and Irreplaceability** — Conversations with Tyler · via Conversations with Tyler  
why: _Diamond and Cowen debate whether leadership matters more than luck in shaping history._  
field: history-of-thought · topic: — · school: — · format: — · level: — · era: timeless · region: global  
speakers: Tyler Cowen, Jared Diamond · discussed: Genghis Khan  
tags: historical contingency, human history, irreplaceability, leadership, luck vs agency, network effects, roman empire

**Michael Moritz on Origin Stories, Exile, and Obsessive Curiosity** — Conversations with Tyler · via Conversations with Tyler  
why: _A compelling conversation on curiosity, career pivots, and the business stories behind major institutions._  
field: — · topic: — · school: — · format: — · level: — · era: — · region: —  
speakers: Michael Moritz, Tyler Cowen · discussed: Alex Ferguson  
tags: apple history, chrysler, entrepreneurship, exile, family memoir, origin stories, sequoia capital

**Luke Burgis on Mimetic Desire, Catholicism, and the Age of Social Contagion** — Conversations with Tyler · via Conversations with Tyler  
why: _Connects mimetic desire and social contagion to economics-adjacent behavior and cultural dynamics._  
field: behavioral · topic: — · school: — · format: podcast-episode · level: intermediate · era: — · region: —  
speakers: Luke Burgis, Tyler · discussed: René Girard  
tags: catholicism, girardian theory, human wants, imitation, mimetic desire, religious institutions, social contagion

**Revisiting the China Shock (with Joseph Francis)** — EconTalk · via EconTalk  
why: _Reassesses the empirical basis of the China-shock jobs narrative and its policy implications._  
field: international, labor · topic: china-economy · school: empirical · format: — · level: — · era: — · region: china, us  
speakers: Joseph Francis, Russ Roberts · discussed: David Autor, David Dorn, Gordon Hanson  
tags: causal inference, china shock, import competition, labor-market adjustment, local labor markets, manufacturing jobs, trade exposure

**How Your Situation Shapes You (with Angela Duckworth)** — EconTalk · via EconTalk  
why: _Explores how environment shapes habits and motivation, tying psychology to behavioral economics._  
field: behavioral · topic: — · school: behavioral · format: — · level: — · era: timeless · region: —  
speakers: Angela Duckworth, Russ Roberts · discussed: Angela Duckworth  
tags: behavioral economics, choice architecture, grit, habit formation, motivation, self-control, social environment, willpower

**Lives Wasted and Well-Lived: David Wolpe on The Death of Ivan Ilyich** — EconTalk · via EconTalk  
why: _A reflective discussion on mortality and a well-lived life, using Tolstoy to provoke ethical thinking._  
field: — · topic: — · school: — · format: podcast-episode · level: — · era: timeless · region: —  
speakers: Russ Roberts, David Wolpe · discussed: Leo Tolstoy, Ivan Ilyich  
tags: deathbed reflections, end-of-life care, ethical living, literature and economics, meaning of life, moral philosophy

**The Great Fertility Collapse (with Jesus Fernandez-Villaverde)** — EconTalk · via EconTalk  
why: _Explains why fertility is falling globally and how demographics reshape growth and labor markets._  
field: development · topic: economic-growth · school: — · format: — · level: — · era: — · region: latin-america  
speakers: Jesus Fernandez-Villaverde · discussed: —  
tags: demographic transition, dependency ratio, economic growth, fertility decline, household investment, human capital, labor supply, population aging

**Addiction, Faith, and the Limits of Willpower (with Meghan O'Gieblyn)** — EconTalk · via EconTalk  
why: _Explores addiction and self-control through behavioral perspectives and philosophy-influenced insights._  
field: behavioral · topic: — · school: behavioral · format: — · level: — · era: — · region: —  
speakers: Russ Roberts, Meghan O'Gieblyn · discussed: Meghan O'Gieblyn, Simone Weil, William James, Iris Murdoch  
tags: addiction, behavioral economics, faith, health behavior, self-control, time inconsistency, willpower

**Public Choice and Politics Without Romance (with Mike Munger)** — EconTalk · via EconTalk  
why: _A crisp public-choice critique of government power and political incentives._  
field: public · topic: regulation · school: public-choice · format: — · level: — · era: timeless · region: —  
speakers: Russ Roberts, Mike Munger · discussed: Mike Munger  
tags: munger test, political incentives, public agency problems, public choice, regulatory capture, rent-seeking

**The Death of Reading (with James Marriott)** — EconTalk · via EconTalk  
why: _Connects the economics of attention and human capital to democracy and civic resilience._  
field: — · topic: — · school: — · format: — · level: — · era: — · region: global  
speakers: James Marriott, Russ Roberts · discussed: James Marriott  
tags: civic knowledge, democracy, information consumption, media, reading decline

**Incentives Are for Losers (with Adam Mastroianni)** — EconTalk · via EconTalk  
why: _Explores when incentive-following becomes morally wrong and how psychology reshapes economic thinking._  
field: behavioral · topic: — · school: behavioral · format: — · level: intermediate · era: timeless · region: —  
speakers: Adam Mastroianni, Russ Roberts · discussed: Adam Mastroianni  
tags: behavioral ethics, cheating, incentives, lying for incentives, moral hazard, psychology of decision-making, temptation

## topics frequency

inequality (11), ai-economy (10), regulation (6), china-economy (5), tariffs (5), interest-rates (5), economic-growth (4), healthcare (4), national-debt (3), taxation (3), the-fed (3), housing (3), socialism-vs-capitalism (2), inflation (2), price-system (1), gold-standard (1), privatization (1), entrepreneurship (1), bitcoin (1), 2008-crisis (1)

## fields frequency

history-of-thought (16), innovation (15), public (15), international (14), macro (12), labor (12), behavioral (12), trade (7), business (7), micro (6), fiscal-macro (6), health-education-welfare (6), law-econ (5), private-markets (4), rates (4), markets-investing (3), monetary-policy (3), urban-housing (3), environment-energy (3), money-bitcoin (3), finance (2), intl-finance (2), development (2), sound-money (2), general (2), credit (2), quantitative (1), economic-history (1), business-cycles (1), equities (1), transition (1), industrial-org (1), macro-investing (1)

## schools frequency

behavioral (9), empirical (5), classical-liberal (4), keynesian (1), public-choice (1), marxist (1), new-institutional (1)

## format frequency

podcast-episode (10), explainer (1), interview (1)

## level frequency

intermediate (23), expert (1)

## Tag vocabulary (905 distinct; ≥2 uses shown)

inequality (15), hoover institution (11), productivity (10), incentives (8), public policy (8), behavioral economics (6), causal inference (5), tax policy (5), political economy (5), globalization (5), risk management (4), trade policy (4), human capital (4), rent-seeking (4), labor displacement (4), supply chains (4), book review (4), policy evaluation (3), automation (3), regulatory capture (3), economic incentives (3), economic policy (3), federal reserve (3), austerity (3), eurozone (3), private equity (3), stanford siepr (3), income inequality (3), market design (3), distributional effects (3), representation (3), cooperation (3), consumer preferences (3), pricing (3), intellectual history (3), economic-growth (2), future-of-work (2), price signals (2), gold standard (2), microfoundations (2), institutional-design (2), china shock (2), import competition (2), labor-market impacts (2), local labor markets (2), technology adoption (2), habit formation (2), self-control (2), willpower (2), dependency ratio (2), economic growth (2), labor supply (2), population aging (2), budget constraints (2), fiscal sustainability (2), inflation risk (2), public choice (2), democracy (2), fiscal policy (2), wealth tax (2), capital markets (2), securities regulation (2), education policy (2), school choice (2), cold war legacy (2), inflation (2), monetary policy (2), civil society (2), free markets (2), corporate governance (2), wage inequality (2), credit conditions (2), task displacement (2), financial regulation (2), economic stagnation (2), european politics (2), capital allocation (2), intergenerational inequality (2), consumer behavior (2), family law (2), sanctions (2), trade restrictions (2), political-economy (2), market power (2), decoupling (2), industrial policy (2), demographics (2), prediction markets (2), capitalism critique (2), germany (2), property rights (2), ai automation (2), capitalism (2), liberal democracy (2), inflation dynamics (2), tariffs (2), protectionism (2), matching markets (2), moral economics (2), information asymmetry (2), medical mistrust (2), classical liberalism (2), public-choice (2), bureau of labor statistics (2), private money (2), stablecoins (2), regulation (2), hybrid work (2), pandemic labor market (2), remote work (2), work-from-home (2), evolutionary psychology (2), public goods (2), freakonomics radio (2), cost-benefit analysis (2), consumer demand (2), innovation incentives (2), social cognition (2), credit risk (2), credit markets (2), yield-curve (2), social psychology (2), intellectuals (2), ideology (2)

## Out-of-vocabulary values the model wanted (candidates for new topics)

- format: [{"v": "podcast-episode", "c": 0.9}] ×50
- format: [{"v": "podcast-episode", "c": 0.95}] ×40
- level: [{"v": "intermediate", "c": 0.6}] ×39
- level: [{"v": "intermediate", "c": 0.55}] ×28
- format: [{"v": "podcast-episode", "c": 0.85}] ×11
- level: [{"v": "intermediate", "c": 0.65}] ×8
- level: [{"v": "introductory", "c": 0.55}] ×8
- level: [{"v": "intermediate", "c": 0.62}] ×7
- level: [{"v": "intermediate", "c": 0.7}] ×7
- topics: {"v": "general", "c": 0.25} ×6
- level: [{"v": "introductory", "c": 0.45}] ×6
- level: [{"v": "introductory", "c": 0.6}] ×5
- format: [] ×5
- level: [] ×5
- format: [{"v": "podcast-episode", "c": 0.93}] ×4
- level: [{"v": "intermediate", "c": 0.45}] ×4
- format: [{"v": "explainer", "c": 0.8}] ×4
- topics: {"v": "development", "c": 0.2} ×3
- format: [{"v": "podcast-episode", "c": 0.92}] ×3
- format: [{"v": "interview", "c": 0.55}, {"v": "podcast-episode", "c" ×3
- format: [{"v": "interview", "c": 0.85}] ×3
- format: [{"v": "explainer", "c": 0.85}] ×3
- topics: {"v": "general", "c": 0.15} ×2
- topics: {"v": "general", "c": 0.3} ×2
- level: [{"v": "introductory", "c": 0.62}] ×2
- topics: {"v": "general", "c": 0.55} ×2
- topics: {"v": "general", "c": 0.5} ×2
- format: [{"v": "podcast-episode", "c": 0.75}] ×2
- format: [{"v": "podcast-episode", "c": 0.88}] ×2
- format: [{"v": "podcast-episode", "c": 0.7}] ×2
- topics: {"v": "general", "c": 0.35} ×2
- format: [{"v": "interview", "c": 0.9}] ×2
- format: [{"v": "speech", "c": 0.7}] ×2
- level: [{"v": "expert", "c": 0.55}] ×2
- format: [{"v": "explainer", "c": 0.78}] ×2
- regions: {"v": "asia", "c": 0.2} ×2
- format: [{"v": "explainer", "c": 0.75}] ×2
- topics: {"v": "social-instinct", "c": 0.0} ×1
- topics: {"v": "economic-history", "c": 0.7} ×1
- topics: {"v": "behavioral", "c": 0.6} ×1
- topics: {"v": "education", "c": 0.65} ×1
- fields: {"v": "education", "c": 0.34} ×1
- topics: {"v": "general", "c": 0.45} ×1
- format: [{"v": "podcast-episode", "c": 0.98}] ×1
- topics: {"v": "economic-history", "c": 0.62} ×1
- topics: {"v": "behavioral", "c": 0.75} ×1
- topics: {"v": "general", "c": 0.6} ×1
- topics: {"v": "environment-energy", "c": 0.22} ×1
- topics: {"v": "alternatives", "c": 0.2} ×1
- topics: {"v": "innovation", "c": 0.3} ×1
- topics: {"v": "innovation", "c": 0.35} ×1
- topics: {"v": "innovation", "c": 0.55} ×1
- level: [{"v": "introductory", "c": 0.35}] ×1
- fields: {"v": "taxation", "c": 0.7} ×1
- fields: {"v": "public-choice", "c": 0.35} ×1
- format: [{"v": "interview", "c": 0.55}, {"v": "lecture", "c": 0.35}] ×1
- format: [{"v": "lecture", "c": 0.72}] ×1
- topics: {"v": "general", "c": 0.2} ×1
- format: [{"v": "lecture", "c": 0.8}] ×1
- format: [{"v": "interview", "c": 0.6}] ×1
