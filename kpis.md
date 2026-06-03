# KPI Matematis untuk Sales Planner

Berikut formulasi matematis KPI yang relevan untuk Sales Planner pada simulasi S&OP beserta:

* definisi,
* interpretasi,
* asumsi,
* dan keterbatasannya.

Formula disusun berdasarkan logika simulasi pada tutorial S&OP. 

---

# 1. Revenue

## Tujuan

Mengukur total pendapatan penjualan.

---

## Formula

[
Revenue_t = P_t \times UnitsSold_t
]

Dimana:

* (P_t) = selling price pada periode (t)
* (UnitsSold_t) = unit yang berhasil dijual

---

## Asumsi

1. Semua unit terjual pada harga yang sama.
2. Tidak ada:

   * diskon per segmen,
   * tax,
   * multi-product pricing.
3. Revenue hanya berasal dari sales utama.

---

## Interpretasi

| Nilai  | Makna                           |
| ------ | ------------------------------- |
| Tinggi | volume dan/atau price tinggi    |
| Rendah | demand rendah atau harga rendah |

---

# 2. Revenue Growth (RG)

## Tujuan

Mengukur pertumbuhan revenue antar periode.

---

## Formula

[
RG_t =
\frac{
Revenue_t - Revenue_{t-1}
}{
Revenue_{t-1}
}
]

atau dalam persen:

[
RG_t(%) =
\left(
\frac{
Revenue_t - Revenue_{t-1}
}{
Revenue_{t-1}
}
\right)\times100
]

---

## Asumsi

1. Revenue periode sebelumnya tidak nol.
2. Growth dianggap meaningful antar bulan.
3. Tidak mempertimbangkan seasonality secara eksplisit.

---

## Interpretasi

| Nilai    | Makna       |
| -------- | ----------- |
| (RG > 0) | growth      |
| (RG < 0) | contraction |

---

# 3. Gross Margin (GM)

## Tujuan

Mengukur profitability pricing.

---

## Formula

[
GM_t =
\frac{
Revenue_t - COGS_t
}{
Revenue_t
}
]

---

## Dengan:

[
COGS_t =
UnitsSold_t \times UnitCost
]

---

## Bentuk Expanded

[
GM_t =
\frac{
(P_t \times UnitsSold_t)
------------------------

(UnitCost \times UnitsSold_t)
}{
P_t \times UnitsSold_t
}
]

---

## Simplified

[
GM_t =
\frac{
P_t - UnitCost
}{
P_t
}
]

(jika seluruh unit sold memiliki cost sama)

---

## Asumsi

1. Unit cost konstan.
2. Tidak ada variable manufacturing complexity.
3. Tidak memasukkan holding cost & penalty.

---

## Interpretasi

| Nilai  | Makna              |
| ------ | ------------------ |
| Tinggi | pricing sehat      |
| Rendah | excessive discount |

---

# 4. Operating Profit

## Tujuan

Mengukur profit akhir sistem.

---

## Formula

[
Profit_t =
Revenue_t
---------

(
COGS_t
+
HoldingCost_t
+
Penalty_t
)
]

---

## Dengan

### Holding Cost

[
HoldingCost_t =
EndingInventory_t
\times HoldingRate
]

---

### Stockout Penalty

[
Penalty_t =
MissedDemand_t
\times PenaltyRate
]

---

## Asumsi

1. Holding cost linear.
2. Penalty linear terhadap unmet demand.
3. Tidak ada fixed operating expense.

---

# 5. Market Share (MS)

## Tujuan

Mengukur posisi kompetitif.

---

## Formula

[
MS_t =
\frac{
FirmDemand_t
}{
TotalMarketDemand_t
}
]

---

## Alternatif

Jika menggunakan actual sales:

[
MS_t =
\frac{
UnitsSold_t
}{
TotalMarketSales_t
}
]

---

## Asumsi

1. Market size observable.
2. Hanya ada dua competitor utama.
3. Tidak ada segmentation market.

---

## Interpretasi

| Nilai  | Makna                |
| ------ | -------------------- |
| Tinggi | market dominance     |
| Rendah | weak competitiveness |

---

# 6. Market Share Momentum (MSM)

## Tujuan

Mengukur arah perubahan market share.

---

## Formula

[
MSM_t =
MS_t - MS_{t-1}
]

---

## Rolling Version

[
MSM_t =
\frac{
MS_t - MS_{t-3}
}{3}
]

---

## Asumsi

1. Trend lebih penting daripada single-period noise.
2. Market share inertia exists.

---

# 7. Relative Price Index (RPI)

## Tujuan

Mengukur posisi harga relatif terhadap competitor.

---

## Formula

[
RPI_t =
\frac{
P_t - P^c_t
}{
P^c_t
}
]

Dimana:

* (P_t) = company price
* (P^c_t) = competitor price

---

## Interpretasi

| Nilai     | Makna       |
| --------- | ----------- |
| (RPI > 0) | lebih mahal |
| (RPI < 0) | lebih murah |

---

## Asumsi

1. Customer membandingkan relative price.
2. Competitor product dianggap substitutable.

---

# 8. Service Level (SL)

## Tujuan

Mengukur kemampuan memenuhi demand.

---

## Formula

[
SL_t =
\frac{
UnitsSold_t
}{
Demand_t
}
]

---

## Dalam persen

[
SL_t(%) =
\left(
\frac{
UnitsSold_t
}{
Demand_t
}
\right)\times100
]

---

## Asumsi

1. Semua unmet demand dianggap lost sales.
2. Tidak ada backorder.

---

## Interpretasi

| Nilai  | Makna                   |
| ------ | ----------------------- |
| Tinggi | operational reliability |
| Rendah | stockout problem        |

---

# 9. Fill Rate

Dalam simulasi ini fill rate praktis identik dengan service level.

---

## Formula

[
FillRate_t =
\frac{
DemandFulfilled_t
}{
TotalDemand_t
}
]

---

# 10. Stockout Rate (SOR)

## Tujuan

Mengukur severity unmet demand.

---

## Formula

[
SOR_t =
\frac{
MissedDemand_t
}{
Demand_t
}
]

---

## Dengan

[
MissedDemand_t =
\max(0,
Demand_t - UnitsSold_t)
]

---

## Asumsi

1. Semua unmet demand hilang permanen.
2. Tidak ada delayed fulfillment.

---

# 11. Forecast Error (FE)

## Tujuan

Mengukur deviasi forecast.

---

## Formula

[
FE_t =
ActualDemand_t - Forecast_t
]

---

## Interpretasi

| Nilai   | Makna         |
| ------- | ------------- |
| Positif | underforecast |
| Negatif | overforecast  |

---

# 12. Forecast Accuracy (FA)

---

# Menggunakan MAPE

## Step 1 — Absolute Percentage Error

[
APE_t =
\left|
\frac{
Actual_t - Forecast_t
}{
Actual_t
}
\right|
]

---

## Step 2 — MAPE

[
MAPE =
\frac{1}{n}
\sum_{t=1}^{n}
APE_t
]

---

## Step 3 — Forecast Accuracy

[
FA =
1 - MAPE
]

---

## Asumsi

1. Actual demand tidak nol.
2. Error simetris dianggap acceptable.

---

# 13. Forecast Bias

## Tujuan

Mengukur systematic over/under forecasting.

---

## Formula

[
Bias =
\frac{
1}{n}
\sum_{t=1}^{n}
(Actual_t - Forecast_t)
]

---

## Interpretasi

| Nilai   | Makna         |
| ------- | ------------- |
| Positif | underforecast |
| Negatif | overforecast  |

---

# 14. Months of Coverage (MOC)

## Tujuan

Mengukur kecukupan inventory.

---

## Formula

[
MOC_t =
\frac{
PipelineInventory_t
}{
ForecastDemand_t
}
]

---

## Asumsi

1. Forecast reasonable.
2. Demand relatif stabil.

---

## Interpretasi

| Nilai  | Makna          |
| ------ | -------------- |
| Tinggi | overstock risk |
| Rendah | stockout risk  |

---

# 15. Pipeline Inventory

## Formula

[
PipelineInventory_t =
OnHand_t
+
InTransit_t
]

---

# 16. Inventory Turnover

## Tujuan

Mengukur efisiensi inventory utilization.

---

## Formula

[
InventoryTurnover_t =
\frac{
COGS_t
}{
AverageInventory_t
}
]

---

## Dengan

[
AverageInventory_t =
\frac{
BeginningInventory_t
+
EndingInventory_t
}{2}
]

---

## Asumsi

1. Inventory valuation stabil.
2. COGS proportional terhadap sales.

---

# 17. Price Elasticity of Demand

## Tujuan

Mengukur sensitivitas demand terhadap harga.

---

## Formula

[
\epsilon =
\frac{
%\Delta Demand
}{
%\Delta Price
}
]

---

## Expanded

[
\epsilon =
\frac{
(D_2-D_1)/D_1
}{
(P_2-P_1)/P_1
}
]

---

## Interpretasi

| Nilai | Makna    |      |           |
| ----- | -------- | ---- | --------- |
| (     | \epsilon | > 1) | elastic   |
| (     | \epsilon | < 1) | inelastic |

---

# 18. Competitive Pressure Score (Optional)

## Tujuan

Mengukur tekanan pricing kompetitif.

---

## Formula

[
CPS_t =
RPI_t
\times
(-MSM_t)
]

---

## Interpretasi

| Nilai  | Makna                        |
| ------ | ---------------------------- |
| Tinggi | overpriced & losing share    |
| Rendah | competitive position healthy |

---

# 19. Pricing Power Indicator (Optional)

## Tujuan

Mengukur kemampuan menaikkan harga.

---

## Formula

[
PPI_t =
\frac{
GM_t \times SL_t
}{
1 + |MSM_t^-|
}
]

---

## Asumsi

1. Strong service mendukung premium pricing.
2. Market share decline mengurangi pricing power.

---

# Kesimpulan

KPI Sales Planner dapat dibagi menjadi:

| Category                 | KPI                       |
| ------------------------ | ------------------------- |
| Growth                   | Revenue, Revenue Growth   |
| Profitability            | Gross Margin, Profit      |
| Competitive              | Market Share, RPI         |
| Operational Constraint   | Service Level, Stockout   |
| Planning Quality         | Forecast Accuracy, Bias   |
| Inventory Sustainability | MOC, Inventory Turnover   |
| Strategic Pricing        | Elasticity, Pricing Power |

Dan secara matematis pricing problem dapat diringkas sebagai:

[
\max
f(
RevenueGrowth,
GrossMargin,
MarketShare
)
]

dengan constraint:

[
ServiceLevel \ge threshold
]

[
StockoutRisk \le limit
]

[
InventoryCoverage \in acceptable\ range
]
