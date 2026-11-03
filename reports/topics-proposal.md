# Proposed topic list v1 (for owner approval)

Built from the 173-item sample (what the model assigned, what it reached for when no topic fit) plus the
brief's examples. 82 topics, each with a parent Field. **Kept** = already in the 25-item seed.

## Money, banking & macro
inflation (kept) · deflation · stagflation · the-fed (kept) · ecb · bank-of-england · central-bank-independence (kept) ·
interest-rates (kept) · quantitative-easing · money-supply · gold-standard (kept) · bretton-woods · recessions ·
business-cycle · unemployment · great-depression (kept) · 2008-crisis (kept) · banking-crises · bank-runs ·
national-debt (kept) · government-spending · fiscal-stimulus · austerity · sovereign-debt-crises · euro-crisis

## Markets & investing
stock-market · bonds-and-yields · credit-markets · private-equity · venture-capital · hedge-funds · ipos-and-capital-markets ·
asset-bubbles · market-cycles · risk-management · value-investing · commodities · real-estate-investing

## Money & Bitcoin
bitcoin (kept) · stablecoins · cbdc · sound-money · hyperinflation

## Trade & international
tariffs (kept) · free-trade · china-shock · globalization · exchange-rates · dollar-dominance · sanctions-and-economic-statecraft ·
emerging-markets

## Labor, welfare & inequality
minimum-wage (kept) · labor-markets · immigration · inequality (kept) · poverty · welfare-state · pensions-and-social-security ·
education (new: model reached for it repeatedly) · school-choice · universal-basic-income

## Public policy & regulation
taxation (kept) · wealth-tax · regulation (kept) · antitrust · industrial-policy · housing (kept) · zoning-and-land-use ·
healthcare (kept) · energy-and-climate · price-controls · rent-control

## Systems, institutions & history
price-system (kept) · socialism-vs-capitalism (kept) · central-planning · privatization (kept) · shock-therapy (kept) ·
property-rights · rule-of-law · public-choice-government-failure · industrial-revolution · economic-history-of-europe ·
polish-economy · soviet-economy

## Growth, technology & business
economic-growth (kept) · productivity · ai-economy (kept) · innovation · entrepreneurship (kept) · china-economy (kept) ·
development-and-poverty-traps · state-capacity

## Thought & method
history-of-economic-thought · keynes-vs-hayek · rational-expectations · behavioral-economics · econometrics-and-causal-inference ·
economics-of-science

## Merges / changes from the seed
- `privatization` and `shock-therapy` kept separate (Polish sources need both).
- Fields stay coarse; topics carry the specificity. Field-like values the model put in topics (general, innovation, development) are now either real topics (innovation) or dropped.
- New regions requested by the model: **france, spain, germany, asia** → proposed additions (Region facet).
- People: the model sometimes lists institutions ("Federal Reserve") as people → prompt fix: people = humans only.

## Known sample errors (for judging quality)
- Sowell *School Choice* → topic "inequality" (should be education / school-choice: both now added).
- *Teaching Gorbachev Capitalism* panel → field empty (low confidence; would be systems / transition).
- *A Price Is a Signal* (MRU explainer) → format missing (should be explainer).
