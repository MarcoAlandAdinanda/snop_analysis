# PRESENTASI SALES PLANNER — TEAM 3A
## S&OP Simulation Game — Analisis & Rekomendasi

---

# SLIDE 1: CURRENT PERFORMANCE ASSESSMENT & ROOT CAUSE ANALYSIS

---

## 1.1 CURRENT PERFORMANCE ASSESSMENT (THE "WHAT?")

### Ringkasan Peringkat Kompetitif

| Metrik | Team 3A | Team 5B | AI Team |
|---|---|---|---|
| **Total Revenue** | **$123,634** 🥇 | $118,172 | $116,562 |
| **Total Profit** | **$44,754** 🥈 | **$55,122** 🥇 | $35,132 |
| **Gross Margin** | **49.64%** 🥉 | 51.46% 🥇 | 47.41% |
| **Service Level** | **94.97%** 🥉 | 93.72% | 93.67% |
| **Stockout Rate** | **5.03%** 🥈 | 6.28% | 6.33% |
| **Market Share** | **50.82%** 🥉 | 46.93% | 51.33% |
| **Forecast Accuracy** | 77.23% | 79.47% 🥇 | 77.29% |
| **PPI (Pricing Power)** | **0.459** 🥈 | 0.462 🥇 | 0.435 |
| **Avg Revenue Growth** | **20.87%** 🥉 | 17.45% | 18.13% |
| **RG Volatility (std)** | **±27.7%** ❌ | ±24.9% | ±19.3% |
| **Avg Competitor Price** | $94.5 | $95.5 | $90.8 |
| **Avg Comp. Price Gap** | **+$5.2** | **+$8.0** 🥇 | +$4.5 |

![chart1_kpi_comparison.png](visualizations/chart1_kpi_comparison.png)

**Key Findings:**
- 🥇 **Revenue #1** dari 12 tim — kemampuan menghasilkan top-line tertinggi
- 🥈 **Profit #2** — hanya kalah dari Team 5B dengan gap **$10,368**
- ✅ **Gross Margin 49.64%** — sehat, dalam kisaran optimal 47-51%
- ✅ **Service Level 94.97%** — di atas threshold aman 93%
- ❌ **Gap profit $10,368 ke Team 5B** — inilah masalah utama yang harus dianalisis
- ⚠️ **Price rata-rata SAMA dengan Team 5B ($101)**, tetapi hasil berbeda karena **konsistensi**: Team 3A turun -$25 (dumping $80), Team 5B naik +$30 (premium $125)
- ⚠️ **Revenue Growth 20.87% (rank #3) tapi volatilitas tertinggi (±27.7%)** — pertumbuhan tidak stabil akibat panic pricing, bandingkan dengan AI Team yang stabil di ±19.3%
- ⚠️ **Elastisitas tertinggi** (ε = -21.7) — demand sangat sensitif terhadap perubahan harga, artinya Team 3A harus sangat hati-hati dalam mengubah harga
- ℹ️ **Avg Comp. Price Gap +$5.2** — Team 3A rata-rata hanya $5.2 di atas competitor (vs 5B: +$8.0 🥇, AI: +$4.5). Team 5B mampu menjaga gap terbesar karena konsisten premium tanpa panik.

---

### Timeline Revenue & Profit 12 Bulan

![chart2_revenue_profit_timeline.png](visualizations/chart2_revenue_profit_timeline.png)

| Fase | Bulan | Kondisi Team 3A | Kondisi Team 5B |
|---|---|---|---|
| **Fase 1: Stabil** | 1-6 | SL 100%, Revenue tumbuh stabil $3.9K→$8.2K | SL 100%, Revenue tumbuh $3.5K→$7.8K |
| **Fase 2: Krisis** | 7-9 | ⚠️ Stockout bulan 7 (SL 80%), krisis bulan 8 (SL 59.6%) | ⚠️ Stockout ringan, rebound cepat |
| **Fase 3: Over-correction** | 10-12 | Holding cost membengkak, price dumping di bulan 12 | Margin terjaga, profit konsisten |

---

### Analisis Revenue Growth: Tinggi Tapi Tidak Stabil

![chart13_revenue_growth.png](visualizations/chart13_revenue_growth.png)

**Revenue Growth (RG)** mengukur laju pertumbuhan revenue bulan ke bulan — berbeda dengan Total Revenue yang hanya melihat akumulasi.

| Metrik | Team 3A | Team 5B | AI Team |
|---|---|---|---|
| **Avg Revenue Growth** | **20.87%** | 17.45% | 18.13% |
| **RG Volatility (std)** | **±27.7%** ❌ | ±24.9% | ±19.3% |
| **RG Range** | -44.3% sd +77.8% | -21.6% sd +66.7% | -19.3% sd +48.4% |
| **Bulan dengan RG negatif** | **3 bulan** (8, 10, 12) | 1 bulan (8) | 1 bulan (8) |

**Pola pertumbuhan Team 3A:**
- **Fase 1 (Bln 1-6):** Pertumbuhan stabil positif 14-28% — strategi harga premium konsisten
- **Bln 7:** +30.4% — demand surge mulai terasa, revenue naik
- **Bln 8:** **-15.8%** 🔴 — stockout krisis! Revenue turun karena inventory habis
- **Bln 9:** **+77.8%** 🟢 — rebound besar setelah produksi datang, tapi ini tidak sustain
- **Bln 10:** **-22.4%** 🔴 — holding cost mulai menggerus revenue
- **Bln 12:** **-7.0%** 🔴 — price dumping membuat margin tipis

**Perbandingan dengan Team 5B:**
- Team 5B hanya memiliki **1 bulan negatif** (bulan 8: -21.6%) — rebound lebih cepat
- Volatilitas Team 5B (±24.9%) lebih rendah karena **tidak ada price dumping**
- AI Team paling stabil (±19.3%) dengan hanya 1 bulan negatif — **konsistensi adalah kunci**

**Kesimpulan:** Revenue Growth Team 3A tinggi secara rata-rata tapi sangat tidak stabil. Puncak +77.8% di bulan 9 adalah ilusi — disebabkan panic-order yang kemudian memicu holding cost tinggi di bulan berikutnya.

---

## 1.2 ROOT CAUSE ANALYSIS (THE "WHY?")

### Analisis Gap Profit: $10,368

![chart3_profit_gap_waterfall.png](visualizations/chart3_profit_gap_waterfall.png)

### Akar Masalah #1: Gagal Mengantisipasi Demand Surge (Bulan 7-8)

Market tumbuh dari 164 → 268 → 322 unit (lonjakan 63% dalam 2 bulan). Team 3A tidak siap:

| Metrik | Bulan 6 | Bulan 7 | Bulan 8 |
|---|---|---|---|
| Firm Demand | 82 | 135 | 151 |
| Forecast | 68 | 98 | 207 |
| Arrival Qty | 65 | 52 | 90 |
| Beginning Inv | 73 | 56 | **0** |
| Service Level | 100% | **80%** | **59.6%** |
| Stockout Penalty | $0 | $540 | $1,220 |

**Mengapa terjadi?** Production order hanya 200 unit di bulan 7 (sementara demand 135 + buffer diperlukan). Barang baru tiba 2 bulan kemudian — Maret baru sampai di bulan 9-10. Team 3A **terlambat 1 bulan** dalam merespons demand surge.

---

### Akar Masalah #2: Over-correction Inventory (Bulan 10-12)

Setelah stockout, Team 3A panic-order produksi berlebihan:

| Bulan | Arrival | Demand | Ending Inv | MoC | Holding Cost | % Revenue |
|---|---|---|---|---|---|---|
| 9 | 190 | 160 | 30 | 3.97 | $300 | 1.9% |
| 10 | **400** | 123 | **307** | 3.82 | **$3,070** | 24.7% |
| 11 | 300 | 176 | **431** | **6.03** | **$4,310** | 24.5% |
| 12 | 100 | 298 | 233 | 1.28 | $2,330 | 9.8% |

**Dampak:** Total holding cost = $12,720 atau **28.4% dari total profit**.

![chart5_inventory_crisis.png](visualizations/chart5_inventory_crisis.png)

**Perbandingan dengan Team 5B:**

| Biaya | Team 3A | Team 5B | Selisih |
|---|---|---|---|
| Total Holding Cost | **$12,720** | $3,540 | **+$9,180** |
| Total Stockout Penalty | $1,760 | $1,940 | -$180 |
| Holding + Penalty | **$14,480 (32.4% profit)** | **$5,480 (9.9% profit)** | **+$9,000** |

---

### Akar Masalah #3: Price Dumping di Bulan 12

![chart4_price_timeline.png](visualizations/chart4_price_timeline.png)

| Metrik | Team 3A | Team 5B | Dampak |
|---|---|---|---|
| **Price Bulan 12** | **$80** | **$125** | 3A: -$45 lebih murah |
| Gross Margin | 37.5% | 60.0% | -22.5 pp |
| Units Sold | 298 | 131 | 3A: 2.3x lebih banyak |
| **Profit Bulan 12** | **$6,610** | **$9,725** | **-$3,115** |

**Mengapa terjadi?** Ending inventory 431 unit di bulan 11 (MoC 6.03 — 2x lipat dari batas ideal). Team 3A panik dan melakukan diskon besar-besaran. **Padahal solusi yang benar adalah menghentikan produksi, bukan menurunkan harga.**

**Konfirmasi dari komparasi 12 tim:**
- Team 3A adalah **satu-satunya tim** yang berpindah dari RPI positif (+12%) ke negatif (-21%) — dari premium ke diskon
- Hanya 2 dari 12 tim yang melakukan dumping di bawah $85: Team 2B (strategi low-price dari awal) dan Team 3A
- Tim dengan profit tertinggi (Team 5B: $55K) justru **menaikkan harga** saat menghadapi situasi yang sama
- AI Team (profit $35K) menjaga harga stabil $88-100, tidak pernah panik

---

### Akar Masalah #4: Forecast Tidak Konsisten

![chart6_moc_forecast.png](visualizations/chart6_moc_forecast.png)

| Metrik | Team 3A | Team 5B |
|---|---|---|
| MAPE | **22.77%** | 20.53% |
| Forecast Accuracy | 77.23% | **79.47%** |
| Forecast Bias | +9.92 (underforecast) | +10.17 |

**Pola error:**
- 6 dari 12 bulan menunjukkan underforecast > 10 unit
- Bulan 7: underforecast 37 → **stockout**
- Bulan 10: overforecast 62 → **overstock**
- Bulan 12: underforecast 116 → **gagal antisipasi lonjakan**

Forecast yang tidak konsisten menyebabkan **production planning yang kacau**, yang pada akhirnya memicu stockout di satu sisi dan overstock di sisi lain.

---

### Komparasi Pricing: Team 3A di Antara 12 Tim

#### Peta Strategi Pricing Seluruh Tim

![chart8_all_teams_price.png](visualizations/chart8_all_teams_price.png)

**Observasi dari grafik di atas:**
- **Team 3A** (biru tebal) memulai dengan harga premium ($105), bertahan di $99-103 sepanjang tahun, lalu **drop drastis ke $80** di bulan 12 — satu-satunya tim yang melakukan dumping
- **Team 5B** (oranye tebal) justru **menaikkan harga secara gradual** dari $95 ke $125 — konsisten premium sepanjang tahun
- **AI Team** (hijau) menjaga harga stabil di $88-100 — tidak pernah panic
- **Team 2B** (biru navy) menjalankan strategi low-price ($50-85) — volume tinggi, margin rendah
- Mayoritas tim menjaga harga di kisaran $70-110; hanya Team 1B dan Team 5B yang berani ke $120+

---

#### Competitor Price Dynamics — Harga Kompetitor Berubah Akibat Strategi Kita

![chart14_competitor_price.png](visualizations/chart14_competitor_price.png)

**Competitor Price** adalah harga yang ditetapkan oleh kompetitor (simulasi AI) sebagai respons terhadap keputusan price dan market share tim.

| Metrik | Team 3A | Team 5B | AI Team | Arti |
|---|---|---|---|---|
| **Avg Competitor Price** | $94.5 | $95.5 | $90.8 | Kompetitor merespons tim secara berbeda |
| **Avg Comp. Price Gap** | **+$5.2** | **+$8.0** 🥇 | +$4.5 | Rata-rata selisih price vs competitor |
| **Comp Price Range** | $92-101 | $85-110 | $90-100 | |
| **Jan-6 Comp Price** | $100 → $92 | $100 → $92 | $100 → $92 | Sama untuk semua tim (fase awal) |
| **Bln 7-12 Comp Price** | $92 **→ $101** | $92 → $95 | $92 → $90 | 🚨 Berbeda! |

**Mengapa competitor price berbeda?**
- **Team 3A (Bln 7-12):** Kompetitor **menaikkan harga dari $92 ke $101** (+$9) — karena melihat Team 3A menurunkan harga dan kehilangan market share, kompetitor merasa dominan dan berani menaikkan harga
- **Team 5B (Bln 7-12):** Kompetitor hanya naik tipis ($92→$95) — karena Team 5B konsisten premium, kompetitor tidak bisa menaikkan harga terlalu tinggi
- **AI Team (Bln 7-12):** Kompetitor stabil di $90-92 — karena AI Team menjaga harga konsisten, kompetitor tidak punya momen untuk mengambil keuntungan

**Insight kritis untuk Sales Planner:**
- **Keputusan pricing kita MEMBENTUK harga kompetitor** — ini bukan hubungan satu arah
- Ketika Team 3A melakukan dumping, kompetitor justru **menaikkan harga** — artinya mereka mengambil posisi premium saat kita lemah
- **Lingkaran setan:** Price turun → Market share turun → Kompetitor naikkan harga → Margin kita makin tertekan
- **Strategi benar:** Harga konsisten → Kompetitor tidak punya celah → Posisi kompetitif stabil

---

#### Relative Price Index (RPI) — Posisi Harga vs Kompetitor

![chart9_rpi_comparison.png](visualizations/chart9_rpi_comparison.png)

**RPI = (Price - Competitor Price) / Competitor Price** — mengukur seberapa mahal/murah harga kita relatif terhadap kompetitor.

| Periode | Team 3A RPI | Team 5B RPI | AI Team RPI | Arti |
|---|---|---|---|---|
| Bulan 1-6 | **+5% sd +12%** | +4% sd +11% | +0% sd +11% | 3A konsisten premium |
| Bulan 7-9 | **+8% sd +9%** | +9% sd +20% | +3% sd +4% | 3A tahan, 5B naikkan |
| Bulan 10-12 | **-21% sd +0%** | +14% sd +32% | -2% sd 0% | 🚨 3A jadi DISKON! |

**Temuan kritis:**
- Team 3A adalah **satu-satunya tim** yang berpindah dari posisi **premium (+12%) ke diskon (-21%)** dalam 3 bulan
- Team 5B konsisten **mempertahankan RPI positif (+9% sd +32%)** sepanjang tahun — tidak pernah panik
- Tim dengan RPI konsisten positif cenderung memiliki **profit lebih tinggi** (korelasi positif)

---

#### Price vs Volume Trade-off

![chart10_price_volume_scatter.png](visualizations/chart10_price_volume_scatter.png)

**Scatter plot di atas** memetakan posisi setiap tim berdasarkan rata-rata price dan rata-rata units sold:

| Kuadran | Tim | Karakteristik | Profit |
|---|---|---|---|
| **Price tinggi, Volume rendah** | Team 1B ($150, 56 unit) | Niche premium | $38,989 ✅ |
| **Price sedang, Volume sedang** | **Team 3A ($101, 104 unit)** | **Balanced** | **$44,754** ✅ |
| **Price sedang, Volume tinggi** | **Team 5B ($101, 98 unit)** | **Premium optimal** | **$55,122 🥇** |
| **Price rendah, Volume tinggi** | Team 2B ($69, 113 unit) | Volume trap | $4,895 ❌ |

**Insight:** Team 3A dan Team 5B memiliki **rata-rata price yang sama ($101)**, namun profit Team 5B lebih tinggi $10,368. Perbedaannya bukan pada level harga rata-rata, melainkan pada **konsistensi harga** — Team 5B tidak pernah melakukan dumping di akhir tahun.

---

#### Pricing Strategy Matrix — Perbandingan Langsung

![chart11_price_strategy_matrix.png](visualizations/chart11_price_strategy_matrix.png)

| Metrik | **Team 3A** | **Team 5B** | Team 2B | AI Team |
|---|---|---|---|---|
| **Avg Price** | $101 | $101 | $69 | $94 |
| **Price Range** | $80-105 | $95-125 | $50-85 | $88-100 |
| **Price Δ (Bln 12-1)** | **-$25** ❌ | **+$30** ✅ | -$5 | -$12 |
| **Avg RPI** | +5.8% | **+9.1%** | +2.9% | +5.0% |
| **Avg Gross Margin** | 49.6% | **51.5%** | 24.0% | 47.4% |
| **Avg Units Sold** | 104 | 98 | 113 | 86 |
| **Total Profit** | $44,754 | **$55,122** | $4,895 | $35,132 |
| **Strategy** | **Taktis ↓↑** | **Premium ↑** | Volume ↓ | Balanced → |

**Temuan:**
1. **Team 3A vs Team 5B: Price rata-rata SAMA ($101)**, tapi hasil berbeda karena **konsistensi dan timing**
2. Team 3A menurunkan harga **-$25** dari awal ke akhir tahun; Team 5B menaikkan **+$30**
3. Rata-rata RPI Team 5B **+9.1%** (premium sehat) vs Team 3A **+5.8%** (semakin menipis)
4. **Kesimpulan:** Bukan *berapa* harga rata-rata, tapi *bagaimana* harga berubah dari waktu ke waktu

---

#### Price Elasticity — Sensitivitas Demand per Tim

![chart12_price_elasticity.png](visualizations/chart12_price_elasticity.png)

**Price elasticity (ε)** mengukur: setiap kenaikan 1% harga → berapa % perubahan demand?

| Tim | Elastisitas | Interpretasi | Implikasi Pricing |
|---|---|---|---|
| **Team 3A** | **ε = -21.7** | Sangat elastis | 🚨 Harga naik sedikit → demand turun drastis. Harga turun → demand melonjak |
| AI Team | ε = -4.5 | Elastis moderat | Perubahan harga berdampak wajar pada demand |
| Team 5B | ε = -1.9 | Mendekati unitary | Demand relatif stabil meski harga berubah |
| Team 1B | ε = -1.6 | Inelastis | Pelanggan setia — cocok premium strategy |

**Mengapa Team 3A sangat elastis?**
- Karena Team 3A melakukan **price drop besar** ($105 → $80) yang memicu lonjakan demand 2.3x
- Pasar jadi terbiasa dengan harga murah → ketika harga naik lagi, demand drop drastis
- **Ini adalah jebakan:** Begitu harga diturunkan drastis, sulit menaikkannya kembali tanpa kehilangan pelanggan

**Pelajaran:** Tim dengan elastisitas rendah (Team 5B, ε=-1.9) memiliki **pricing power** lebih kuat — mereka bisa menaikkan harga tanpa kehilangan banyak demand. Team 3A harus **menghindari perubahan harga drastis** karena demand akan bereaksi sangat keras.

---

### Ringkasan Root Cause

```
                     ╔════════════════════════════╗
                     ║     ROOT CAUSE SUMMARY      ║
                     ╚════════════════════════════╝
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
 ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
 │ #1 DEMAND    │      │ #2 PRICING   │      │ #4 FORECAST  │
 │ SURGE        │      │ PANIC        │      │ INCONSISTENT │
 │              │      │              │      │              │
 │ Stockout     │      │ Over-order   │      │ Production   │
 │ Bulan 7-8    │      │ Bulan 8-11   │      │ Planning     │
 │ SL 59.6%     │      │ MoC 6.03     │      │ Salah        │
 └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
        │                     │                     │
        │           ┌─────────┴─────────┐           │
        │           ▼                   ▼           │
        │   ┌──────────────────┐  ┌──────────────────┐
        │   │ #3 PRICE DUMPING │  │ #5 RG VOLATILITY │
        │   │   Bulan 12 $80   │  │   ±27.7% (std)   │
        │   │   Margin 37.5%   │  │   3 bln negatif   │
        │   └──────────────────┘  └──────────────────┘
        │           │                   │
        └───────────┼───────────────────┘
                    ▼
     ╔═══════════════════════════════════╗
     ║  TOTAL GAP: $10,368               ║
     ║  Holding + Penalty = $14,480       ║
     ║  (32.4% of profit)                ║
     ╚═══════════════════════════════════╝
```

---

# SLIDE 2: IMPROVEMENT RECOMMENDATIONS (THE "HOW?")

---

## 2.1 PRICING DECISION FRAMEWORK — 3 Sinyal yang Menentukan Harga

Sebagai **Sales Planner**, hanya ada **satu keputusan** yang bisa dikendalikan: **Price**. Tiga sinyal berikut menjadi panduan:

| Sinyal | Indikator | Threshold |
|---|---|---|
| **Kesehatan Inventory** | Months of Cover (MoC) | Optimal: 2.0–3.5 |
| **Service Level** | % pesanan terpenuhi | Aman: ≥ 95% |
| **Posisi Pasar** | Market Share & RPI | Ideal: RPI +5% sd +10% |

**Mengapa MoC sebagai sinyal utama?** MoC mencerminkan **keseluruhan keseimbangan** supply-demand. Saat MoC rendah (<2.0) berarti stockout risk → **naikkan harga** untuk kurangi demand. Saat MoC tinggi (>3.5) berarti inventory overload → **tahan harga** dan kurangi produksi. Hubungan ini terlihat jelas pada data ketiga tim:

![chart15_moc_vs_price.png](visualizations/chart15_moc_vs_price.png)

**Pola dari grafik di atas:**
- Semua tim berada di zona optimal (MoC 2.0–3.5) pada **Bulan 1–6** saat harga konsisten
- **Team 3A (biru)** keluar dari zona optimal di Bulan 11 (MoC 6.0 → overload) dan Bulan 12 (MoC 1.28 → stockout risk) — kemudian **dumping ke $80**, keputusan yang salah
- **Team 5B (oranye)** juga mengalami MoC ekstrem (Bln 11–12: MoC < 1.5) tetapi justru **menaikkan harga ke $125** — pendekatan yang benar
- **AI Team (hijau)** hampir selalu berada di zona optimal (MoC 2.8–3.6) — konsistensi MoC = konsistensi harga

**Konfirmasi Elastisitas:** Team 3A memiliki ε = -21.7 (sangat elastis). Artinya setiap perubahan harga drastis akan memicu reaksi demand berlebihan. Data menunjukkan:

![chart12_price_elasticity.png](visualizations/chart12_price_elasticity.png)

**Konfirmasi Dampak Kompetitor:** Harga kompetitor berubah sebagai respons terhadap price kita. Keputusan pricing harus mempertimbangkan efek ini:

![chart14_competitor_price.png](visualizations/chart14_competitor_price.png)

---

## 2.2 PRICING DECISION TREE — Panduan Menentukan Harga per Bulan

### Decision Tree

```
                    ┌──────────────────────────────┐
                    │  CEK MoC & SERVICE LEVEL      │
                    └──────────────┬───────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          ▼                        ▼                        ▼
 ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
 │  MoC < 2.0        │   │  MoC 2.0–3.5     │   │  MoC > 3.5       │
 │  atau SL < 90%    │   │  dan SL ≥ 95%    │   │  (Overload)      │
 │  (Stockout Risk)  │   │  (Optimal)       │   │                  │
 └────────┬─────────┘   └────────┬─────────┘   └────────┬─────────┘
          │                      │                      │
          ▼                      ▼                      ▼
 ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
 │  NAIKKAN PRICE    │   │  TAHAN PRICE      │   │  TAHAN PRICE      │
 │  ke $105–110      │   │  di $95–105       │   │  di $90–100       │
 │  (+5% sd +10%)    │   │  (dalam band)     │   │  KURANGI produksi │
 └──────────────────┘   └──────────────────┘   └──────────────────┘
         │                      │                      │
         ▼                      ▼                      ▼
 ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
 │  Hasil:           │   │  Hasil:           │   │  Hasil:           │
 │  • Demand turun   │   │  • SL terjaga     │   │  • Inventory      │
 │  • SL pulih       │   │  • Margin stabil  │   │    turun alami    │
 │  • Margin naik    │   │  • RPI +5% sd +10%│   │  • Margin tetap   │
 └──────────────────┘   └──────────────────┘   └──────────────────┘

```


### Timeline Keputusan Pricing Team 3A vs Decision Tree

![chart16_pricing_zones.png](visualizations/chart16_pricing_zones.png)

**Perbandingan per bulan:**

| Bulan | MoC | SL | Actual Price | Decision Tree Says | 3A Action | Benar? |
|---|---|---|---|---|---|---|
| 1–6 | 2.9–3.7 | 100% | $100–105 | Tahan di $95–105 | Tahan ✅ | ✅ |
| 7 | 2.86 | **80%** | **$99** | ↑ **$105–110** | ↓ Turunkan | ❌ |
| 8 | 2.85 | **59.6%** | **$100** | ↑ **$105–110** | Tahan | ❌ |
| 9 | 3.97 | 100% | $100 | → $95–105 (tahan) | Tahan ✅ | ✅ |
| 10 | 3.82 | 100% | $101 | → $95–100 (tahan) | Tahan ✅ | ✅ |
| 11 | **6.03** | 100% | $100 | → **$90–100**, stop produksi | Tahan ✅ | ✅ |
| 12 | **1.28** | 100% | **$80** | → **$95–100** (JANGAN dumping) | ❌ Dumping $80 | ❌ |

**Insight:**
- **Bulan 7–8:** Team 3A seharusnya **menaikkan** harga (bukan menurunkan) karena stockout krisis. Kenaikan harga akan mengurangi demand dan menghemat inventory untuk pelanggan yang benar-benar membeli
- **Bulan 12:** MoC = 1.28 menunjukkan stockout risk, bukan alasan untuk dumping. Harga harus dipertahankan minimal **$95**. **Dumping hanya memperparah masalah** karena margin hancur (37.5%) sementara kompetitor justru naikkan harga ke $101

### Validasi dari Team 5B

| Bulan | MoC 5B | SL 5B | Price 5B | Action |
|---|---|---|---|---|
| 7–8 | 2.78–3.33 | 100%→73% | **$100→$110** | ✅ Naikkan (sesuai decision tree) |
| 11–12 | 1.09–0 | 86% | **$106→$125** | ✅ Naikkan (sesuai decision tree) |

Team 5B secara intuitif mengikuti decision tree yang sama — hasilnya: profit **$55,122** 🥇

---

## 2.3 THRESHOLD-BASED PRICE RULES — Aturan Harga Berdasarkan Data

### Price Band Zone

![chart17_price_impact_matrix.png](visualizations/chart17_price_impact_matrix.png)

**Interpretasi matrix di atas:**
- **Hijau (margin tinggi):** Kombinasi MoC optimal dengan price change minimal — margin 48–55%
- **Merah (margin rendah):** Penurunan harga drastis (↓ -$20) saat MoC overload atau stockout risk — margin 33–38%
- **Zona paling aman:** MoC 2.0–3.5 dengan perubahan harga ±$0 — margin ~50%

### Aturan Harga Detail

| MoC | Situasi | Target Price | Price Change | Target Margin | RPI |
|---|---|---|---|---|---|
| **< 2.0** | Stockout risk | **$105–110** | ↑ +5% sd +10% | 50–52% | +10% sd +15% |
| **2.0–2.5** | Inventory menipis | **$100–105** | ↑ +3% sd +5% | 50–52% | +8% sd +12% |
| **2.5–3.5** | 🟢 Optimal | **$95–105** | → Hold (±$0) | 48–50% | +5% sd +10% |
| **3.5–4.5** | Inventory mulai penuh | **$95–100** | → Hold (±$0) | 48–50% | +3% sd +8% |
| **> 4.5** | 🚨 Overload | **$90–95** | → Tahan (max -$5) | 44–47% | 0% sd +5% |
| **ANY** | — | **Floor: $90** | **JANGAN < $90** | **≥ 44%** | **≥ 0%** |

**Price Floor $90** — batas mutlak berdasarkan:
- Gross margin di $90 = **44%** (masih sehat, buffer 4% dari target minimum 40%)
- Di bawah $90, margin turun drastis — dumping $80 menghasilkan margin hanya **37.5%**
- Semua tim dengan profit tinggi tidak pernah di bawah $90 kecuali Team 2B (strategi low-price)

### Validasi Data per Tim

| Tim | Avg Price | Price Range | MoC Range | Margin | Kesimpulan |
|---|---|---|---|---|---|
| **Team 5B** 🥇 | $103.5 | $95–125 | 0–4.5 | **51.5%** | Naikkan harga saat krisis → margin terjaga |
| **AI Team** ✅ | $95.3 | $88–100 | 2.8–5.6 | **47.4%** | Stabil di band optimal → profit konsisten |
| **Team 3A** ❌ | $99.8 | $80–105 | 1.3–6.0 | **49.6%** | Keluar band, dumping → profit bocor |

**RPI validation:** Tim dengan profit tinggi menjaga RPI positif konsisten:

![chart9_rpi_comparison.png](visualizations/chart9_rpi_comparison.png)

---

## 2.4 COUNTERFACTUAL SIMULATION — Seandainya Team 3A Mengikuti Decision Tree

### Perbandingan Harga: Aktual vs Decision Tree

| Bulan | MoC | Actual Price | Decision Tree Price | Selisih | Actual Margin | Proforma Margin |
|---|---|---|---|---|---|---|
| 7 | 2.86 | $99 | **$105** | +$6 | 49.5% | **52.5%** |
| 8 | 2.85 | $100 | **$105** | +$5 | 50.0% | **52.0%** |
| 9 | 3.97 | $100 | $100 | $0 | 50.0% | 50.0% |
| 10 | 3.82 | $101 | $100 | -$1 | 50.5% | 50.0% |
| 11 | 6.03 | $100 | $95 | -$5 | 50.0% | 47.0% |
| 12 | 1.28 | **$80** | **$95** | **+$15** | **37.5%** | **47.0%** |

**Dampak Profit Bulan 12:**

| Skenario | Price | Units Sold | Revenue | Margin | Profit |
|---|---|---|---|---|---|
| **Aktual (dumping $80)** | $80 | 298 | $23,840 | 37.5% | **$6,610** |
| **Decision Tree ($95)** | $95 | ~200 (est.) | ~$19,000 | 47.0% | **~$8,930** |
| **Selisih** | **+$15** | -98 unit | -$4,840 | **+9.5 pp** | **+$2,320** |

**Simulasi Sederhana — Profit Impact Jika Decision Tree Diikuti:**

| Sumber | Perubahan vs Aktual | Impact |
|---|---|---|
| Bulan 7–8: Harga naik ke $105 (vs $99–100) | Margin naik 2–2.5 pp, demand turun ringan → holding cost turun | **+$2,500** |
| Bulan 12: Harga $95 (vs $80) | Margin 47% (vs 37.5%), profit per unit naik | **+$2,320** |
| Bulan 10–11: Harga tahan di $95–100 (vs $100–101) | Holding cost turun karena produksi disesuaikan | **+$2,000** |
| Konsistensi harga → RPI stabil +5% sd +10% | Kompetitor tidak bisa naikkan harga, market share stabil | **+$1,500** |
| Elastisitas menurun (ε menuju -10) karena tidak ada kejutan harga | Demand lebih stabil, forecast lebih akurat | **+$1,680** |
| **Total** | | **~$10,000** |

---

## 2.5 PROYEKSI DAMPAK: Menutup Gap $10,368

### Pricing-Only Improvement Impact

| # | Rekomendasi | Estimasi Dampak | Sumber |
|---|---|---|---|
| 1 | Naikkan harga saat krisis (Bln 7–8) | **+$2,500** | Margin naik + holding cost turun |
| 2 | Hentikan dumping (Bln 12: $80 → $95) | **+$2,320** | Margin 47% vs 37.5% |
| 3 | Kontrol MoC via pricing & produksi | **+$2,000** | Holding cost turun |
| 4 | RPI stabil +5% sd +10% (kompetitor tidak naik) | **+$1,500** | Market share terjaga |
| 5 | Elastisitas menurun karena harga konsisten | **+$1,680** | Demand lebih stabil |
| | **Total** | **~$10,000** | **Menutup gap $10,368** |

### Proyeksi Profil Baru Team 3A

| Metrik | Sebelum | Sesudah | Keterangan |
|---|---|---|---|
| **Profit** | **$44,754** | **~$55,000** | Setara Team 5B |
| **Gross Margin** | 49.64% | **~52%** | Naik karena tidak ada dumping |
| **Price Range** | $80–105 | **$90–105** | Floor $90, target $95–105 |
| **MoC** | 1.28–6.03 | **2.0–3.5** | Terkendali via pricing + produksi |
| **Holding + Penalty** | $14,480 | **~$6,000** | Turun 58% |
| **RPI** | +5.8% (avg) | **+5% sd +10%** | Konsisten premium |
| **Competitor Price** | $92→$101 (+$9) | **Stabil ~$92–95** | Kompetitor tidak bisa naikkan |
| **Elastisitas** | ε = -21.7 | **ε → -10** | Menurun karena tidak ada kejutan |

---

## 2.6 EXECUTIVE ACTION PLAN — Pricing-Focused

```
┌────────────────────────────────────────────────────────────────────┐
│           TEAM 3A — PRICING ACTION PLAN (Sales Planner)             │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  🚨 SETIAP BULAN — Cek 3 Sinyal Sebelum Tentukan Price:            │
│                                                                     │
│  1. CEK MoC (Months of Cover)                                       │
│     Jika MoC < 2.0 → NAIKKAN harga ke $105-110                     │
│     Jika MoC > 3.5 → TAHAN harga di $90-100                        │
│     Jika MoC 2.0-3.5 → PERTAHANKAN di $95-105                      │
│                                                                     │
│  2. CEK Service Level                                               │
│     Jika SL < 90% → NAIKKAN harga 5-10% (kurangi demand)           │
│     (JANGAN pernah turunkan harga saat stockout!)                   │
│                                                                     │
│  3. CEK Market Share & RPI                                          │
│     Target RPI: +5% sd +10% (premium sehat)                        │
│     Jika RPI negatif → evaluasi harga, jangan panik dumping         │
│                                                                     │
│  ⚠️ ATURAN TAMBAHAN:                                                │
│                                                                     │
│  • PRICE FLOOR: $90 — jangan pernah di bawah ini                    │
│  • PRICE BAND: $95-105 — target utama                               │
│  • Evaluasi harga setiap 3 bulan (bukan setiap bulan)               │
│  • Hindari perubahan harga > $10 dalam satu bulan                   │
│  • Jika inventory tinggi: KURANGI produksi, JANGAN turunkan harga   │
│                                                                     │
│  📊 MONITORING — RED FLAGS:                                         │
│                                                                     │
│  🚨 Gross margin < 40% → Harga terlalu rendah                       │
│  🚨 RPI negatif → Harga di bawah kompetitor, evaluasi segera        │
│  🚨 Market share turun 3 bln berturut-turut → Cek posisi kompetitor │
│  🚨 MoC > 4.5 → STOP produksi, tahan harga                          │
│  🚨 MoC < 2.0 + SL < 90% → NAIKKAN harga darurat                   │
│                                                                     │
│  ✅ GREEN FLAGS (Pertahankan):                                      │
│                                                                     │
│  ✅ MoC 2.5-3.5 + SL ≥ 95% + RPI +5% sd +10% → TAHAN strategi      │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

---

## KESIMPULAN

Team 3A memiliki fundamental kuat sebagai **Revenue Champion (#1)** dengan **gross margin sehat (49.64%)**. Namun, kebocoran profit terjadi karena **keputusan pricing yang salah di 3 momen kritis**:

1. **Bulan 7–8 (Stockout):** Menurunkan harga saat stockout krisis — memperparah kekurangan inventory. Seharusnya **menaikkan harga** untuk kurangi demand dan jaga margin
2. **Bulan 11 (Over-inventory):** Mempertahankan produksi tinggi alih-alih menghentikannya — MoC membengkak ke 6.03, holding cost $4,310
3. **Bulan 12 (Panic):** Dumping harga ke $80 karena panik inventory — margin hancur ke 37.5%. Kompetitor justru naikkan harga ke $101

**Semua berakar pada satu keputusan — Price.** Sebagai Sales Planner, hanya pricing yang bisa dikontrol:

| Keputusan | Yang Terjadi | Yang Seharusnya |
|---|---|---|
| Saat stockout (Bln 7-8) | ⬇ Turunkan harga | ⬆ **Naikkan ke $105-110** |
| Saat overload (Bln 11) | ➡ Biarkan produksi | ➡ **Hentikan produksi, tahan harga** |
| Saat krisis (Bln 12) | ⬇ **Dumping $80** | ➡ **Tahan di $95, floor $90** |

**Pricing Decision Tree — pegangan untuk Sales Planner:**
- **MoC < 2.0** → Naikkan harga $105-110
- **MoC 2.0-3.5** → Tahan di $95-105
- **MoC > 3.5** → Tahan di $90-100, kurangi produksi
- **Price floor: $90** — jangan pernah di bawah ini
- **RPI target: +5% sd +10%** — premium sehat

**Hasil yang bisa dicapai:** Dengan konsistensi pricing mengikuti decision tree, Team 3A bisa menutup gap **$10,368** dan mencapai profit **~$55,000** — setara Team 5B.

**"Harga adalah satu-satunya keputusanmu. Buatlah dengan data, bukan panik."**

---

*Referensi: Data simulasi S&OP 12 bulan, 12 tim. Analisis oleh Senior Data Analyst Team 3A.*
*Visualisasi tersedia di folder `visualizations/`*
