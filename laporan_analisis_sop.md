# Laporan Analisis S&OP — Sales Planner Pricing Decision

## 1. Pendahuluan

### 1.1 Latar Belakang

Sales & Operations Planning (S&OP) adalah proses integrasi antara perencanaan penjualan, operasi, inventory, dan finansial yang bertujuan menyelaraskan **supply** dan **demand** dalam satu rencana bisnis yang terpadu. Dalam simulasi S&OP yang dianalisis, setiap tim berperan sebagai **Sales Planner** yang bertanggung jawab menentukan:

- **Harga jual** (*selling price*) setiap periode
- **Production order** untuk memenuhi demand
- **Keseimbangan** antara service level, inventory coverage, dan profitabilitas

### 1.2 Tujuan Analisis

1. Menghitung dan membandingkan **19 KPI** dari setiap tim selama 12 periode
2. Mengidentifikasi **feature non-KPI** yang paling berpengaruh terhadap KPI Sales Planner
3. Memberikan rekomendasi **feature set optimal** untuk model prediktif pricing
4. Menyusun insight strategis untuk pengambilan keputusan pricing

### 1.3 Ruang Lingkup

| Aspek | Detail |
|-------|--------|
| **Jumlah tim** | 12 tim (11 tim peserta + 1 AI Team sebagai benchmark) |
| **Periode** | 12 bulan |
| **Skenario** | Kompetisi duopoly dengan competitor pricing dinamis |
| **Total observasi** | 144 baris data (12 tim × 12 bulan) |
| **Tools** | Python (Pandas, Scikit-learn, Matplotlib, Seaborn) |

---

## 2. Metodologi

### 2.1 Alur Analisis

```
Raw Data (df_history_display_all_players.csv)
        │
        ▼
   KPI Engineering ────→ 19 KPI (berdasarkan kpis.md)
        │
        ▼
   KPI Summary ────────→ Aggregasi per tim (mean/sum)
        │
        ▼
   Feature Selection ──→ 3 metode korelasi (Pearson, Spearman, MI)
        │                    │
        │                    ▼
        │              Composite Scoring + Elbow Method
        │                    │
        │                    ▼
        │              Domain Knowledge Overlay
        │                    │
        │                    ▼
        │              Validasi Random Forest (5-fold CV)
        │
        ▼
   Insight & Rekomendasi
```

### 2.2 Definisi KPI

Berdasarkan panduan `kpis.md`, KPI Sales Planner dikelompokkan dalam 7 kategori:

| Kategori | KPI |
|----------|-----|
| **Growth** | Revenue, Revenue Growth |
| **Profitability** | Gross Margin, Operating Profit |
| **Competitive** | Market Share, Relative Price Index (RPI) |
| **Operational Constraint** | Service Level, Stockout Rate, Fill Rate |
| **Planning Quality** | Forecast Accuracy (MAPE), Forecast Bias |
| **Inventory Sustainability** | Months of Coverage, Inventory Turnover |
| **Strategic Pricing** | Price Elasticity, Competitive Pressure Score (CPS), Pricing Power Indicator (PPI) |

Formulasi matematis setiap KPI mengacu pada `kpis.md` dan telah diimplementasikan dalam notebook `01_generate_kpi.ipynb`.

---

## 3. Ringkasan KPI Seluruh Tim

### 3.1 Tabel KPI Summary

| Team | Revenue | Profit | Gross Margin | Service Level | Stockout Rate | Market Share | RPI | MAPE | Forecast Acc |
|------|---------|--------|-------------|--------------|--------------|-------------|-----|------|-------------|
| **AI Team** | 116,562 | 35,132 | 47.41% | 93.67% | 6.33% | 51.33% | 0.050 | 22.71% | 77.29% |
| Team 1A | 95,680 | 32,630 | 44.35% | 90.08% | 9.92% | 47.41% | 0.069 | 18.83% | 81.17% |
| Team 1B | 76,149 | 38,989 | 54.41% | 84.45% | 15.55% | 34.53% | 0.293 | 32.96% | 67.04% |
| Team 2A | 95,626 | 24,916 | 39.11% | 94.90% | 5.10% | 50.20% | 0.076 | 20.91% | 79.09% |
| Team 2B | 94,985 | 4,895 | 24.04% | 98.85% | 1.15% | 55.62% | 0.029 | 34.69% | 65.31% |
| **Team 3A** | **123,634** | **44,754** | **49.64%** | 94.97% | 5.03% | 50.82% | 0.058 | 22.77% | 77.23% |
| Team 4A | 93,912 | 35,342 | 46.67% | 79.66% | 20.34% | 48.97% | 0.029 | 17.57% | 82.43% |
| Team 4B | 101,445 | 28,195 | 38.34% | 95.26% | 4.74% | 52.61% | 0.048 | 18.05% | 81.95% |
| Team 5A | 99,909 | 27,409 | 38.68% | 97.21% | 2.79% | 50.17% | 0.069 | 15.39% | 84.61% |
| **Team 5B** | **118,172** | **55,122** | **51.46%** | 93.72% | 6.28% | 46.93% | 0.091 | 20.53% | 79.47% |
| Team 6A | 99,083 | 35,053 | 44.39% | 82.52% | 17.48% | 50.35% | 0.016 | 14.82% | 85.18% |
| Team 6B | 92,095 | 17,285 | 33.21% | 92.45% | 7.55% | 51.50% | 0.033 | 26.82% | 73.18% |

### 3.2 Peringkat Tim berdasarkan Key Metrics

#### Revenue Tertinggi
| Rank | Team | Total Revenue |
|------|------|-------------|
| 1 | **Team 3A** | **123,634** |
| 2 | Team 5B | 118,172 |
| 3 | AI Team | 116,562 |

#### Profit Tertinggi
| Rank | Team | Total Profit |
|------|------|-------------|
| 1 | **Team 5B** | **55,122** |
| 2 | Team 3A | 44,754 |
| 3 | Team 1B | 38,989 |

#### Service Level Tertinggi
| Rank | Team | Service Level |
|------|------|-------------|
| 1 | Team 2B | 98.85% |
| 2 | Team 5A | 97.21% |
| 3 | Team 4B | 95.26% |

#### Forecast Accuracy Tertinggi (1 - MAPE)
| Rank | Team | Forecast Accuracy |
|------|------|-----------------|
| 1 | Team 6A | 85.18% |
| 2 | Team 5A | 84.61% |
| 3 | Team 4A | 82.43% |

### 3.3 Insight Awal

- **Team 5B** memiliki profit tertinggi ($55,122$) meskipun revenue nomor 2 — ini menunjukkan efisiensi operasional dan strategi pricing yang unggul (Gross Margin 51.46%)
- **AI Team** memiliki performa konsisten di semua metrik (balanced) — tidak terbaik di satu kategori tetapi solid di semua lini
- **Team 2B** memiliki Service Level tertinggi (98.85%) namun profit terendah ($4,895$) — indikasi *over-inventory* dan *harga terlalu rendah*
- **Team 4A** memiliki Service Level terendah (79.66%) dengan Stockout Rate 20.34% — menunjukkan masalah serius dalam inventory management
- **Team 6A** memiliki forecast accuracy tertinggi (85.18%) tetapi hanya peringkat menengah dalam profit — akurasi forecast tidak menjamin profitabilitas tanpa strategi pricing yang tepat

---

## 4. Analisis Per Kategori KPI

### 4.1 Growth — Revenue & Revenue Growth

#### Tren Revenue per Tim

Revenue seluruh tim menunjukkan pola meningkat dari bulan 1-12, namun dengan akselerasi yang berbeda:

- **Team 3A** mencapai revenue tertinggi dengan growth agresif di bulan 9-12 (dari 16K ke 23.8K)
- **Team 6A** memiliki **Revenue Growth rata-rata tertinggi** (103.19%) karena strategi *low-to-high price transition*
- **AI Team** growth stabil (18.13%) dengan konsistensi tinggi

Strategi pricing agresif di bulan 7-12 terbukti efektif untuk tim yang berani menaikkan harga di atas competitor.

### 4.2 Profitability — Gross Margin & Operating Profit

| Team | Gross Margin | Operating Profit | Insight |
|------|-------------|-----------------|---------|
| Team 1B | **54.41%** | $38,989 | Margin tinggi, profit sehat |
| Team 5B | **51.46%** | **$55,122** | Margin & profit optimal |
| Team 3A | 49.64% | $44,754 | Balance margin-volume |
| Team 2B | 24.04% | $4,895 | Margin rendah — pricing terlalu murah |

**Trade-off terlihat jelas**: Tim dengan Gross Margin tinggi cenderung memiliki market share lebih rendah, dan sebaliknya. Team 5B adalah satu-satunya yang berhasil menyeimbangkan keduanya.

### 4.3 Competitive — Market Share, RPI, CPS

#### Market Share vs Relative Price Index

| Tim | Market Share | RPI | Strategi |
|-----|-------------|-----|----------|
| Team 2B | 55.62% | 0.029 | Harga hampir sama dengan kompetitor, fokus volume |
| AI Team | 51.33% | 0.050 | Premium tipis, volume tetap tinggi |
| Team 1B | 34.53% | 0.293 | Premium tinggi, market share rendah — *niche strategy* |

**RPI positif** berarti harga jual lebih tinggi dari competitor. Team 1B dengan RPI 0.293 (termahal) hanya menguasai 34.53% market share. Ini konsisten dengan teori bahwa **kenaikan harga menekan market share**, namun tim dengan margin tinggi dapat tetap profitabel jika Service Level terjaga.

#### Competitive Pressure Score

CPS mengukur tekanan kompetitif. Tim dengan RPI tinggi dan MS menurun (MSM negatif) memiliki CPS tinggi. Team 1B memiliki CPS tertinggi (0.057) — indikasi *overpriced & losing share*. AI Team memiliki CPS sangat rendah (0.0008) — posisi kompetitif sehat.

### 4.4 Operational — Service Level & Stockout

#### Service Level Trend

Insiden stockout massal terjadi di **bulan 7-9** di hampir semua tim, dipicu oleh lonjakan demand (total market naik dari 164 ke 384). Tim yang bertahan:

| Tim | SL Bulan 8 | Stockout Rate | Strategi |
|-----|-----------|--------------|----------|
| Team 2B | 100% | 1.15% | Inventory buffer besar |
| Team 5A | 100% | 2.79% | Balanced approach |
| Team 4A | 70.4% | 20.34% | Stockout parah — kurang inventory |

AI Team mengalami penurunan SL ke 58.5% di bulan 8 — momen kritis yang disebabkan oleh forecast error tinggi (underforecast 64 unit).

### 4.5 Planning Quality — Forecast Accuracy & Bias

| Tim | MAPE | Forecast Bias | Interpretation |
|-----|------|--------------|----------------|
| Team 6A | 14.82% | +1.17 | Underforecast ringan |
| Team 5A | 15.39% | +4.83 | Underforecast moderat |
| Team 4A | 17.57% | +20.25 | Underforecast signifikan |
| Team 1B | 32.96% | +13.92 | Akurasi rendah, bias positif |
| Team 2B | 34.69% | -11.83 | Overforecast sistematis |

**Pola dominan**: Sebagian besar tim memiliki **forecast bias positif** (underforecast), yang konsisten dengan lonjakan demand di akhir tahun. Hanya Team 2B yang overforecast sistematis, yang menjelaskan inventory berlebih mereka.

### 4.6 Inventory — Months of Coverage & Turnover

| Tim | Avg Months of Cover | Inventory Turnover | Interpretasi |
|-----|-------------------|-------------------|--------------|
| AI Team | 3.51 | 79.36 | Ideal (3-4 bulan) |
| Team 5B | 2.75 | 110.91 | Agresif, turnover tinggi |
| Team 2B | 3.59 | 286.68 | Overstock, turnover tidak wajar |
| Team 4A | 2.41 | 112.12 | Stockout risk |

**Target ideal**: 3 bulan coverage. AI Team konsisten di kisaran ini. Team 2B memiliki MoC 3.59 namun turnover 286.68 yang mengindikasikan inventory fluctuation ekstrem — inventory menumpuk di awal lalu habis di akhir.

### 4.7 Strategic Pricing — Price Elasticity & PPI

#### Price Elasticity

| Tim | Avg Elasticity | Interpretasi |
|-----|---------------|--------------|
| Team 3A | -21.73 | Sangat elastis — demand sensitif terhadap harga |
| Team 4A | +4.05 | Inelastis — demand tidak responsif (anomali) |
| AI Team | -4.45 | Elastis moderat |

Nilai elastisitas yang sangat tinggi pada Team 3A disebabkan oleh strategi price drop drastis di bulan 8 yang memicu lonjakan demand besar-besaran. Ini menunjukkan bahwa **market ini sangat price-sensitive**.

#### Pricing Power Indicator (PPI)

PPI mengukur kemampuan menaikkan harga tanpa kehilangan market share.

| Tim | PPI | Interpretasi |
|-----|-----|-------------|
| Team 1B | 0.478 | Pricing power kuat — margin tinggi + SL cukup |
| Team 5B | 0.462 | Pricing power kuat |
| AI Team | 0.435 | Pricing power moderat |
| Team 2B | 0.206 | Pricing power lemah — margin rendah |

Team 1B mampu mempertahankan margin tertinggi meskipun market share rendah karena **service level yang cukup** dan **diferensiasi harga** yang jelas dari competitor.

---

## 5. Feature Selection untuk Sales Planner

### 5.1 Pendekatan

Untuk menentukan variabel non-KPI mana yang paling informatif dalam memprediksi KPI Sales Planner, dilakukan analisis multivariat dengan **3 metode korelasi**:

1. **Pearson r** — hubungan linear
2. **Spearman ρ** — hubungan monotonik
3. **Mutual Information** — hubungan non-linear umum

### 5.2 9 KPI Terpilih untuk Sales Planner

| # | KPI | Kategori | Relevansi dengan Pricing |
|---|-----|----------|-------------------------|
| 1 | `revenue_growth` | Growth | Target utama pricing |
| 2 | `gross_margin` | Profitability | (P - Cost)/P, fungsi langsung price |
| 3 | `operating_profit` | Profitability | Tujuan bisnis akhir |
| 4 | `market_share` | Competitive | Harga → posisi kompetitif |
| 5 | `rpi` | Competitive | Posisi harga relatif ke kompetitor |
| 6 | `service_level` | Operational | Harga tinggi → SL naik, harga rendah → SL turun |
| 7 | `price_elasticity` | Strategic | Sensitivitas demand terhadap price |
| 8 | `ppi` | Strategic | Kemampuan menaikkan harga |
| 9 | `cps` | Strategic | Tekanan kompetitif |

### 5.3 Composite Score & Ranking

Setelah normalisasi dan agregasi 3 metode korelasi terhadap 9 KPI, diperoleh ranking fitur berikut:

| Rank | Feature | Composite Score | Pearson \|r\| | Spearman ρ | MI Score | Source |
|------|---------|:--------------:|:-------------:|:----------:|:--------:|:------:|
| 1 | **price** | **0.3527** | 0.4338 | 0.4140 | 0.5143 | elbow |
| 2 | **competitor_price** | **0.2238** | 0.2959 | 0.2901 | 0.1914 | domain |
| 3 | **cogs_amt** | **0.2131** | 0.2786 | 0.2839 | 0.1701 | domain |
| 4 | **firm_demand** | **0.2022** | 0.2474 | 0.2717 | 0.2038 | domain |
| 5 | **unit_cost** | **0.0010** | 0.0000 | 0.0000 | 0.0080 | domain |

### 5.4 Elbow Method

Elbow method mendeteksi titik optimal pada rank ke-1, artinya hanya **`price`** yang terpilih secara statistik sebagai fitur dengan marginal gain signifikan. Namun, secara domain knowledge, 4 fitur tambahan ditambahkan:

- **`competitor_price`** — anchor keputusan pricing
- **`cogs_amt`** — total biaya produksi
- **`firm_demand`** — volume demand
- **`unit_cost`** — cost dasar

### 5.5 Validasi Random Forest

Untuk memvalidasi kualitas feature set, dilakukan perbandingan RMSE menggunakan **Random Forest dengan 5-fold GroupKFold** (group-by team untuk mencegah data leakage):

| KPI | All Features (20) | Selected (1) | Final (5) |
|-----|:-----------------:|:------------:|:---------:|
| revenue_growth | 0.3929 | 0.5090 | **0.4258** |
| gross_margin | 0.0308 | **0.0247** | 0.0276 |
| operating_profit | 1312.10 | 2195.41 | **1389.83** |
| market_share | **0.0508** | 0.0889 | 0.0687 |
| rpi | 0.0850 | 0.1375 | **0.0802** |
| service_level | **0.0457** | 0.2109 | 0.1185 |
| price_elasticity | **12.6141** | 12.0120 | 11.1670 |
| ppi | **0.0547** | 0.0938 | 0.0701 |
| cps | **0.0197** | 0.0249 | 0.0211 |

| Konfigurasi | Avg RMSE | Std RMSE |
|-------------|:--------:|:--------:|
| All Features (20) | **158.8990** | 48.4970 |
| Selected (1) — `price` only | 245.1783 | 51.3070 |
| Final (5) — `price` + 4 domain | 168.4194 | 55.8553 |

**Interpretasi Validasi:**
- **All Features (20)** memberikan RMSE terendah rata-rata, tetapi berisiko overfitting dan tidak praktis
- **Selected (1)** terlalu sederhana — hanya `price` tidak cukup untuk menangkap kompleksitas S&OP
- **Final (5)** menawarkan **keseimbangan optimal** antara akurasi dan interpretability, dengan performa mendekati All Features pada sebagian besar KPI

---

## 6. Temuan & Insight Strategis

### 6.1 Pricing — Trade-off Utama dalam S&OP

```
                    Price ↑
                   /      \
                  /        \
         Market Share ↓    Gross Margin ↑
              |                  |
              ▼                  ▼
         Demand ↓ ←────────── Profit ?
              |
              ▼
    Service Level ↑ (inventory cukup)
    Stockout ↓
```

Keputusan pricing bukan sekadar menaikkan atau menurunkan harga, melainkan **optimasi multivariat** yang memengaruhi:

1. **Revenue** = Price × Units Sold (kenaikan price bisa menekan volume)
2. **Gross Margin** = (Price - Cost) / Price (hubungan langsung)
3. **Market Share** (elastisitas negatif)
4. **Service Level** (harga rendah → demand tinggi → stockout risk)
5. **Holding Cost & Penalty** (efek tidak langsung)

### 6.2 Pola Strategi Tim

Dari klusterisasi strategi tim, teridentifikasi 3 kelompok utama:

#### Kelompok 1: Premium Pricers (Margin Tinggi, Share Rendah)
- **Tim**: Team 1B
- **Ciri**: Gross Margin > 50%, Market Share < 40%, RPI tinggi
- **Hasil**: Profit sehat, tetapi rentan kehilangan pasar
- **Lesson**: Cocok untuk niche strategy dengan cost control ketat

#### Kelompok 2: Volume Players (Margin Rendah, Share Tinggi)
- **Tim**: Team 2B
- **Ciri**: Gross Margin rendah, Market Share > 55%, Service Level tinggi
- **Hasil**: Profit rendah akibat margin tipis
- **Lesson**: Strategi volume-only tidak sustainable tanpa efisiensi biaya

#### Kelompok 3: Balanced Optimizers (Optimal)

| Tim | Revenue | Profit | Margin | SL | MS |
|-----|---------|--------|--------|----|----|
| **AI Team** | 116.6K | 35.1K | 47.4% | 93.7% | 51.3% |
| **Team 3A** | 123.6K | 44.8K | 49.6% | 95.0% | 50.8% |
| **Team 5B** | 118.2K | 55.1K | 51.5% | 93.7% | 46.9% |

**Ketiga tim ini menunjukkan bahwa keseimbangan antara margin dan volume menghasilkan profit optimal.** Team 5B menjadi benchmark dengan profit tertinggi.

### 6.3 Lonjakan Demand Bulan 7-9 — Momen Kritis S&OP

Bulan 7-9 menampilkan lonjakan total market dari 268 menjadi 384. Tim yang berhasil:

- **AI Team**: Meskipun sempat stockout (SL 58.5% di bulan 8), berhasil rebound di bulan 9 (SL 79.8%) dengan production order agresif (700 unit)
- **Team 5B**: Menggunakan AI price recommendation (95-100) untuk mempertahankan margin sambil tetap memenuhi demand
- **Team 2B**: Over-react dengan inventory berlebih di bulan 7-8, holding cost membengkak

**Takeaway**: S&OP harus mengantisipasi **demand surge** dengan:
- Safety stock yang memadai di periode transisi
- Production lead time yang akurat
- Pricing yang fleksibel untuk mengatur demand

### 6.4 Forecast Quality — Root Cause Analysis

```
Forecast Error ↑
       |
       ▼
Production Order Salah
       |
       ├──→ Over Production → Inventory ↑ → Holding Cost ↑ → Profit ↓
       │
       └──→ Under Production → Stockout → Penalty ↑ → Profit ↓ + SL ↓
```

Tim dengan forecast bias positif (underforecast) mengalami stockout di bulan 8-9. Tim dengan bias negatif (overforecast) mengalami holding cost berlebih.

**Rekomendasi**: Tim harus menerapkan **bias correction** pada model forecast, terutama menjelang periode high-demand.

### 6.5 Korelasi Antar KPI — Heatmap Insights

Berdasarkan correlation matrix:

| Pasangan KPI | Korelasi | Interpretasi |
|-------------|:--------:|-------------|
| Service Level ↔ Stockout Rate | **-0.99** | Hampir perfect inverse — validasi formula |
| Gross Margin ↔ Price | **+0.85** | Hubungan linear kuat — margin ditentukan price |
| Market Share ↔ RPI | **-0.72** | Harga lebih tinggi → share turun |
| CPS ↔ MS Momentum | **-0.65** | Tekanan kompetitif tinggi saat share menurun |
| Inventory Turnover ↔ MoC | **-0.48** | Turnover tinggi → coverage rendah |

---

## 7. Rekomendasi

### 7.1 Strategi Pricing Optimal

Berdasarkan analisis, strategi pricing optimal untuk Sales Planner adalah:

1. **Target Gross Margin**: 47-51% (range optimal berdasarkan AI Team, Team 3A, Team 5B)
2. **RPI target**: 0.05 - 0.09 (premium tipis terhadap competitor)
3. **Service Level threshold**: ≥ 93% (untuk menghindari stockout penalty)
4. **Months of Coverage**: 2.5 - 3.5 bulan

### 7.2 Feature Set untuk Model Prediktif

Gunakan **5 fitur final** untuk modeling pricing decision:

| Feature | Peran dalam Model |
|---------|------------------|
| `price` | Variabel keputusan utama |
| `competitor_price` | Anchor eksternal |
| `cogs_amt` | Batas bawah margin |
| `firm_demand` | Volume constraint |
| `unit_cost` | Cost dasar |

Model berbasis 5 fitur ini memberikan performa mendekati full model (20 fitur) dengan **interpretability yang jauh lebih baik**.

### 7.3 Perbaikan Operasional

| Area | Rekomendasi | Target Tim |
|------|-------------|------------|
| **Forecast Accuracy** | Implementasi bias correction, ensemble method | Team 1B, Team 2B |
| **Inventory Management** | Dynamic safety stock berdasarkan demand volatility | Team 4A, Team 1B |
| **Stockout Prevention** | Early warning system saat SL < 90% | Semua tim |
| **Production Planning** | Lead time adjustment berdasarkan supplier reliability | Team 4A, Team 6A |

### 7.4 S&OP Maturity Roadmap

```
Level 1: Reactive
  └── SL < 85%, Stockout > 15%
  └── Team 4A, Team 6A (bulan 6-8)

Level 2: Consistent
  └── SL 85-93%, Stockout 7-15%
  └── Mayoritas tim

Level 3: Optimized
  └── SL > 93%, Stockout < 5%, Profit optimal
  └── AI Team, Team 3A, Team 5B
```

---

## 8. Kesimpulan

1. **S&OP adalah optimization problem multidimensi**: Tidak ada satu KPI yang bisa dioptimalkan secara terpisah. Pricing, inventory, forecast, dan service level saling terkait erat.

2. **`price` adalah fitur paling dominan** dalam menentukan performa KPI Sales Planner (composite score 0.3527 — 56% lebih tinggi dari fitur kedua). Namun, keputusan pricing harus mempertimbangkan `competitor_price`, `firm_demand`, `cogs_amt`, dan `unit_cost`.

3. **Team 5B dan Team 3A adalah benchmark** dengan strategi balanced yang menghasilkan profit tertinggi. AI Team menunjukkan konsistensi dan dapat dijadikan baseline untuk automated decision-making.

4. **Lonjakan demand di bulan 7-9 adalah momen kritis** yang membedakan tim sukses dan tidak. Antisipasi demand surge harus menjadi prioritas dalam S&OP planning.

5. **Forecast accuracy tidak berkorelasi langsung dengan profitabilitas** — tim dengan akurasi forecast tinggi (Team 6A: 85.18%) belum tentu profit tinggi. Yang lebih penting adalah kemampuan merespons forecast error dengan cepat melalui penyesuaian pricing dan production.

6. **Feature set final (5 fitur)** direkomendasikan untuk pengembangan model prediktif pricing, memberikan keseimbangan optimal antara akurasi prediksi dan kemudahan interpretasi.

---

*Laporan disusun berdasarkan hasil analisis data simulasi S&OP selama 12 periode melibatkan 12 tim. Dataset, notebook Jupyter, dan file pendukung tersedia di repositori untuk verifikasi dan pengembangan lebih lanjut.*
