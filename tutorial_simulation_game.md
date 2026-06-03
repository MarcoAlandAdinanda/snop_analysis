Tutorial v.beta.../
Sales & Operations Planning
A SIMULATION GAME
This tutorial explains how to play the S&OP game

1 Understanding the User Interface
The interface is divided into:
• A feedback panel that explains what happened last month.
• A dashboard panel that summarizes performance over time.
• Decision panels for each role.
You should think of the UI as a management cockpit rather than a form to fill out. Every number shown
is there to support a decision. The game is organized as a monthly decision cycle. Each month follows
the same sequence:
• Review results from previous months.
• Make sales pricing decisions.
• Make demand forecasts.
• Make production and inventory decisions.
• Execute the decisions and move to the next month.
The UI enforces this order intentionally. Some decisions are locked until others are completed. This
reflects real-world dependencies between functions.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 2

2 Reading Metrics and Charts
The dashboard is an executive-level view. It answers one question: Is the system performing well over
time?
2.1 Executive Metrics
The top row shows cumulative performance.
• Total Profit: Revenue minus production cost, holding cost, and stockout penalties. This is the
main score of the game.
• Gross Margin %: Profit as a percentage of revenue. This reflects pricing quality and cost
control.
• Forecast Accuracy:
• Ineventory Turnover:
• Service Level: Units sold divided by total demand. This measures how well operations support
sales.
A strong team grows revenue while keeping service level high and inventory costs controlled.
2.2 Revenue Breakdown
This waterfall-style chart explains where profit
comes from.
• Revenue is reduced by cost of goods sold.
• Holding cost penalizes excess inventory.
• Stockout penalties penalize missed demand.
If profit is low, this chart tells you whether the
problem is pricing, overstocking, or stockouts.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 3

2.3 Revenue Growth
This chart compares cumulative revenue against
the competitor.
o A widening gap in your favor means your
strategy is working.
o A flat or declining gap means either pricing or
service level is weak.
It is especially relevant for the sales role, but
operations indirectly influence it through service
level.
2.4 Demand: Actual vs Forecast
This chart compares:
• Actual demand from the market.
• Forecast values entered by the team.
Large and persistent gaps indicate forecasting
bias. Forecast accuracy matters because
inventory decisions depend directly on it.
2.5 Inventory and Stockouts
This chart shows a classic inventory sawtooth
pattern.
• The step line is on-hand inventory.
• Bars represent lost sales due to stockouts.
Frequent stockouts indicate under-ordering or
delayed reactions to demand changes. Very high
inventory without stockouts indicates over-
ordering.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 4

3 Understanding the Simulation Logic
The engine translates decisions into outcomes. It combines market behavior with supply chain
constraints.
3.1 Market Demand
Total market demand evolves over time using a growth curve and seasonal effects. Demand is not
constant, and it cannot be fully controlled. Your firm only captures a share of this market. Market share
is driven by three factors:
• Relative price versus the competitor.
• Popularity (market share), which adds inertia.
• Availabiluty (service level), which rewards reliable fulfillment.
Even a low price cannot fully compensate for repeated stockouts. Likewise, perfect service cannot
overcome extreme overpricing.
3.2 Competitor Behavior
The competitor adapts based on recent market share.
• When market share is balanced, the competitor will attempt to mimic your price.
• When losing share, the competitor discounts aggressively.
• When winning strongly, the competitor raises prices to harvest profit.
This means your decisions shape the competitor’s behavior indirectly.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 5

4 S&OP Planners
4.1 Sales Planner
Primary responsibility: Set the market price to
balance revenue growth and profitability. The Sales
Manager controls only one decision: price. Despite its
simplicity, price has system-wide effects.
Key KPIs for Sales
• Market Share (3-month average). This shows
how attractive your offering is relative to the
competitor. It reacts slowly because customer
behavior has inertia.
• Revenue Growth (3-month average). This
captures short-term momentum. Declining
growth signals pricing or service problems.
• Competitor Price (last month). This is a
reference, not a target. Large gaps invite
aggressive competitor responses.
How Sales Logic Works
• Lower prices increase demand, but only if product availability is reliable.
• Repeated stockouts reduce service level, which directly lowers market share in future months.
• Higher prices improve margin per unit but reduce demand.
How to Read the AI Recommendation
The AI evaluates (i) Recent market share level, (ii) Direction of market share change, (iii)Revenue growth
trend. Based on this, it classifies the situation into recovery, yield, erosion, or stability modes. The
recommended price is a reference anchor, not a command.
Common Sales Mistakes
• Chasing market share with deep discounts while operations cannot support volume.
• Reacting to one bad month instead of observing three-month patterns.
• Ignoring competitor behavior feedback loops.
Good Sales Practices
• Make incremental price changes.
• Coordinate price moves with operations capacity.
• Accept short-term volume loss if it stabilizes profit and forecasts.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 6

4.2 Demand Planner
Primary responsibility: Translate sales strategy into a
realistic demand signal. The forecast is the backbone
of the system. All inventory decisions depend on it.
Key KPIs for Forecasting
• Forecast Accuracy (3-month average): Measures
how close forecasts are to realized demand.
• Average Bias (3-month average): Indicates
systematic over- or under-forecasting.
• Demand Baseline (3-month average): Provides
scale and context for adjustments.
How to Read the AI Recommendation.
The AI forecast combines four elements (i) Recent demand level, (ii) Price impact from the sales
decision, (iii) Bias correction based on recent errors, (iv) Short-term demand trend. Forecasts are
intentionally conservative. Extreme jumps are dampened unless evidence is consistent. Warnings
appear when accuracy drops below a safe threshold or a consistent bias is detected.
Common Forecasting Mistakes
• Simply copying last month’s demand.
• Overreacting to one-time spikes.
• Ignoring the effect of price changes.
Good Forecasting Practices
• Focus on bias reduction before chasing accuracy.
• Ask Sales to explain pricing decision, not just the number.
• Prefer smooth adjustments unless a structural change is clear.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 7

4.3 Supply Planner
Primary responsibility: Ensure product availability at
minimum total cost. Operations controls production
order quantity, but must think two months ahead.
Key KPIs for Operations
• Fill Rate (last month): Percentage of demand
fulfilled. This affects future market share.
• On-Hand Stock: What is immediately available to
sell.
• Pipeline Inventor: On-hand plus all in-transit
orders. This is the true inventory position.
• Months of Coverage: Pipeline divided by forecast
demand.
How Inventory Logic Works
• Production has a fixed two-month lead time. Orders placed today arrive 2 months later.
• Inventory available in a month equals last month’s ending inventory plus any arriving orders.
• Sales are limited by available inventory; unmet demand results in stockouts.
• Stockouts reduce service level and incur penalties, while excess inventory incurs holding costs.
Both reduce profit.
How to Read the AI Recommendation
The AI evaluates: (i) Current on-hand stock (ii) Arrivals next month (iii) Total pipeline coverage relative to
forecast. It targets roughly 2.5 months of coverage after lead-time demand.
Common Operations Mistakes
• Ordering based only on on-hand inventory.
• Ignoring demand during lead time.
• Overcorrecting after a single stockout.
Good Operations Practices
• Think in pipelines, not on-hand stock.
• Trust forecasts unless bias is proven.
• Absorb small forecast errors with inventory buffers.
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 8

5 Parameters and Rules
5.1 Parameters
Category Parameter Value Description Implications
Supply Chain Production lead 2 months Time between placing an order Forces forward-looking
time and receiving inventory inventory planning
Initial inventory 50 units Starting on-hand stock at Month Buffers early demand
1 uncertainty
Pipeline On-hand + in- Total inventory position Correct basis for inventory
inventory transit decisions
Target coverage 2 months Desired pipeline coverage Balances service and cost
Inventory Cost Unit production 50 per unit Cost incurred for each unit sold Sets minimum viable price
cost
Holding cost 10 per unit per Cost of carrying unsold inventory Penalizes over-ordering
month
Stockout 20 per unit Penalty for each unit of unmet Penalizes under-ordering
penalty demand more strongly
Market Demand Base market 1000 units Long-term market capacity Caps total demand
demand
Market growth Logistic (S- Market grows over time Encourages early
curve curve) positioning
Seasonality Quarterly Demand fluctuates by quarter Requires adaptive
factor multipliers forecasting
Market Market share ? = 1.0 Influence of past market share Adds inertia to customer
Competition weight behavior
Service level ? = 0.5 Impact of fulfillment reliability Rewards operational
weight excellence
Price sensitivity ? = 2.0 Weight of relative price in choice Drives competitive pricing
dynamics
Forecasting Baseline Holt’s method History used for bias and trend Smooths short-term noise
Demand
Trend detection Holt’s method Detects short-term demand drift Supports adaptive
forecasts
Bias correction 3 months Adjusts consistent errors Prevents systematic mis-
window planning
S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada 9

5.2  Formula/Decision Rules
Area  Output  Formula (Conceptual)  Key Parameters  Implications
Variable
Market Growth  Total market  Logistic growth ×  Base market demand,  Market expands over time
demand  seasonal factor  growth rate, seasonality  but with limits
Choice Model  Market share  1 / (1 + e^(?utility  ?, ?, ?  Customers choose
|     |     | difference))  | probabilistically  |
| --- | --- | ------------- | ------------------ |
Firm Demand  Firm demand  Total market × firm  Market demand, share  Sales potential before
|     |     | share  | inventory limits  |
| --- | --- | ------ | ----------------- |
Inventory  Available stock  Beginning inventory +  Lead time  Supply constraint
| Availability  |     | arrivals  |     |
| ------------- | --- | --------- | --- |
Actual Sales  Units sold  min(Available stock, firm  Inventory, demand  Sales limited by inventory
demand)
Stockout  Missed  max(0, demand ? units  Demand, inventory  Lost sales
| Volume  | demand  | sold)  |     |
| ------- | ------- | ------ | --- |
Pipeline  Pipeline units  Ending inventory + in- Lead time  True inventory position
| Inventory  |     | transit  |     |
| ---------- | --- | -------- | --- |
Forecast Error  Error  Actual demand ?  Forecast  Measures bias
forecast
Months of  MOC  Pipeline inventory /  Forecast  Inventory adequacy
| Coverage  |     | forecast  | indicator  |
| --------- | --- | --------- | ---------- |
Revenue  Revenue  Units sold × price  Price  Top-line performance
Cost of Goods  COGS  Units sold × unit cost  Unit cost  Variable production cost
Sold
Holding Cost  Holding cost  Ending inventory ×  Holding cost per unit  Penalty for excess stock
holding cost
Stockout  Penalty  Missed demand ×  Stockout penalty  Penalty for poor service
| Penalty  |     | penalty cost  |     |
| -------- | --- | ------------- | --- |
Profit  Operating  Revenue ? (COGS +  All cost parameters  Overall performance
|     | profit  | holding + penalty)  |     |
| --- | ------- | ------------------- | --- |

S&OP Simulation Game | © Budhi S. Wibowo (2025) | Universitas Gadjah Mada
10
