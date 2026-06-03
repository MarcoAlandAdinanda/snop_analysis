# ANALISIS COGS — Margin Problem vs Pricing Decision
## Team 3A S&OP Simulation Game

---

## 1. OBSERVASI: COGS Gap $7,900

| Komponen | Team 3A | Team 5B | Selisih |
|---|---|---|---|
| Revenue | $123,634 | $118,172 | **+$5,462** |
| COGS | **$64,400** | $56,500 | **+$7,900** |
| Gross Profit | $59,234 | $61,672 | -$2,438 |
| Gross Margin % | **49.64%** | **51.46%** | -1.82 pp |

**COGS 3A $7,900 lebih besar dari 5B — tapi ini bukan masalah biaya.**

---

## 2. AKAR #1: Unit Cost Identik ($50/unit)

```csv
Month, Unit_Cost_3A, Unit_Cost_5B
1-12,  $50,         $50
```

Unit_cost = **$50 fixed** untuk semua tim, setiap bulan. Sales Planner **tidak bisa mengontrol** unit cost.

---

## 3. AKAR #2: COGS Tinggi = Volume Tinggi

Karena unit_cost fixed:

```
COGS = units_sold × $50

Team 3A:  1,288 unit × $50 = $64,400
Team 5B:  1,130 unit × $50 = $56,500
Selisih:   158 unit × $50 =  $7,900  ✓
```

### Decomposition Per Bulan

| Bulan | 3A Units | 5B Units | Selisih | Selisih COGS | Catatan |
|---|---|---|---|---|---|
| 1 | 37 | 37 | +0 | $0 | Sama |
| 2 | 42 | 38 | +4 | +$200 | 3A lebih banyak |
| 3 | 53 | 50 | +3 | +$150 | |
| 4 | 53 | 48 | +5 | +$250 | |
| 5 | 66 | 63 | +3 | +$150 | |
| 6 | 82 | 78 | +4 | +$200 | |
| 7 | **108** | 66 | **+42** | **+$2,100** | 🚨 Demand surge — 5B stockout, 3A normal |
| 8 | 90 | **100** | -10 | -$500 | 3A stockout krisis (SL 59.6%) |
| 9 | **160** | 150 | +10 | +$500 | 3A produksi besar datang |
| 10 | 123 | **172** | -49 | -$2,450 | 5B volume tinggi |
| 11 | 176 | **197** | -21 | -$1,050 | 5B volume tinggi |
| 12 | **298** | 131 | **+167** | **+$8,350** | 🚨 3A PRICE DUMPING! |
| **TOTAL** | **1,288** | 1,130 | **+158** | **+$7,900** | |

### Insight Kunci

**Tanpa Bulan 12 (dumping $80):**

```
3A volume tanpa dumping:  1,288 - 298 =  990 unit
5B volume tanpa dumping:  1,130 - 131 =  999 unit
```

**Tanpa dumping, 3A justru menjual LEBIH SEDIKIT dari 5B.**

Artinya:
- **Bulan 12** menyumbang **106%** dari total selisih COGS ($8,350 dari $7,900)
- Selebihnya, 3A menjual relatif sama dengan 5B (selisih -$450 di bulan lainnya)
- **Kesimpulan: Dumping di bulan 12 adalah SATU-SATUNYA penyebab COGS 3A lebih tinggi**

---

## 4. AKAR #3: Volume Tinggi = Price Rendah

### Rantai Kausalitas

```
                ╔══════════════════════════╗
                ║  KEPUTUSAN PRICING        ║
                ║  (dikontrol Sales Planner)║
                ╚══════════════╤═══════════╝
                               │
                               ▼
                     ╔════════════════╗
                     ║  Price = $80   ║
                     ╚════════╤═══════╝
                              │
                              ▼
                    ╔══════════════════╗
                    ║  Demand melonjak  ║
                    ║  (ε = -21.7)      ║
                    ╚════════╤═════════╝
                             │
                             ▼
                   ╔══════════════════╗
                   ║  Units Sold = 298 ║
                   ║  (+167 vs 5B)    ║
                   ╚════════╤═════════╝
                            │
                            ▼
                   ╔══════════════════╗
                   ║  COGS = $14,900  ║
                   ║  (+$8,350 vs 5B)║
                   ╚════════╤═════════╝
                            │
                            ▼
                   ╔══════════════════╗
                   ║  GROSS MARGIN     ║
                   ║  37.5% (terendah)║
                   ╚════════╤═════════╝
                            │
                            ▼
                   ╔══════════════════╗
                   ║  PROFIT = $6,610 ║
                   ║  (-$3,115 vs 5B)║
                   ╚═════════════════╝
```

### Price vs Units — Bulan 12

| Price | Units | Revenue | COGS | Gross Profit | Gross Margin |
|---|---|---|---|---|---|
| **$80** (3A) | 298 | $23,840 | $14,900 | $8,940 | **37.5%** |
| $125 (5B) | 131 | $16,375 | $6,550 | $9,825 | **60.0%** |

**Team 3A menjual 2.3× lebih banyak unit, tapi Gross Profit LEBIH RENDAH.**

---

## 5. BREAK-EVEN ANALYSIS: Price Drop vs Volume yang Dibutuhkan

### Setiap -$1 Price Membutuhkan Tambahan Unit

Unit_cost = $50. Contribution margin per unit = `Price - $50`.

| Price | Contribution/unit | Unit untuk $10,000 profit |
|---|---|---|
| $110 | $60 | 167 |
| $105 | $55 | 182 |
| $100 | $50 | 200 |
| $95 | $45 | 222 |
| $90 | $40 | 250 |
| $85 | $35 | 286 |
| $80 | $30 | 333 |

**Trade-off:** Turunkan price $1 → butuh **~7 unit tambahan** hanya untuk mempertahankan Gross Profit yang sama. Belum termasuk holding cost yang naik karena produksi lebih besar.

### Counterfactual Bulan 12

| Skenario | Price | Units | Revenue | COGS | GP | HC | Profit |
|---|---|---|---|---|---|---|---|
| **Aktual (dumping)** | $80 | 298 | $23,840 | $14,900 | $8,940 | $2,330 | **$6,610** |
| **Decision Tree** | $95 | ~200 | $19,000 | $10,000 | $9,000 | ~$500 | **~$8,500** |
| **Selisih** | **+$15** | -98 | -$4,840 | -$4,900 | **+$60** | -$1,830 | **+$1,890** |

**Dengan harga $95, profit lebih tinggi +$1,890 meskipun volume turun 33%.**

---

## 6. ELASTISITAS: Mengapa Price Drop Tidak Menguntungkan

| Tim | Elastisitas | Arti |
|---|---|---|
| **Team 3A** | **ε = -21.7** | 1% penurunan price → 21.7% kenaikan demand |
| Team 5B | ε = -1.9 | 1% penurunan price → hanya 1.9% kenaikan demand |

**Aplikasi di Bulan 12:**

```
Price turun 23.8% (dari $105 ke $80)
→ 23.8 × 21.7 = +517% demand (secara elastisitas)
→ Realitanya: demand naik dari ~100 ke 298 = +198%

Artinya: Demand 3A super sensitif terhadap perubahan harga.
Kenaikan volume tidak pernah cukup untuk mengompensasi
penurunan margin per unit.
```

### Visual: Price vs Profit per Unit

| Price | Revenue/Unit | Cost/Unit | Profit/Unit | Units for $10K |
|---|---|---|---|---|
| $105 | $105 | $50 | **$55** | 182 |
| $100 | $100 | $50 | **$50** | 200 |
| $95 | $95 | $50 | **$45** | 222 |
| $90 | $90 | $50 | **$40** | 250 |
| **$80** | **$80** | **$50** | **$30** | **333** |

Pada $80, 3A harus menjual **333 unit** untuk mencapai $10,000 gross profit. Aktualnya hanya 298 unit — dan holding cost $2,330 menggerus profit menjadi hanya $6,610.

---

## 7. RINGKASAN RANTAI KASUALITAS

```
COGS 3A lebih tinggi $7,900
  ↓
BUKAN karena unit cost mahal (sama $50)
  ↓
TAPI karena volume lebih tinggi (1,288 vs 1,130)
  ↓
BUKAN karena demand organik lebih tinggi
  ↓
TAPI karena price dumping ($80) di bulan 12
  ↓
BUKAN karena terpaksa (inventory overload)
  ↓
TAPI karena keputusan pricing yang salah
  ↓
SOLUSI: Pricing Decision Tree
  ├─ MoC < 2.0 → NAIKKAN harga (jangan dumping)
  ├─ MoC 2.0-3.5 → TAHAN harga
  ├─ MoC > 3.5 → TAHAN harga, kurangi produksi
  └─ Price Floor: $90 (margin minimum 44%)
```

---

## 8. KESIMPULAN UNTUK SALES PLANNER

1. **COGS bukan masalah biaya** — ini masalah pricing. Unit_cost fixed, volume naik karena price turun.

2. **Dumping tidak pernah menguntungkan** — setiap -$1 price butuh ~7 unit tambahan hanya untuk break-even. Dengan elastisitas ε=-21.7, volume naik memang besar, tapi margin per unit turun lebih cepat.

3. **Fokus pada margin, bukan volume** — Team 5B menjual lebih sedikit unit (1,130 vs 1,288) tapi profit lebih tinggi ($55,122 vs $44,754). Kuncinya: **price premium dan konsisten**.

4. **Decision Tree sebagai panduan** — jangan pernah membuat keputusan pricing berdasarkan panic. Gunakan MoC sebagai acuan objektif.

---

*Bersumber dari `df_kpi_all_players.csv` — Analisis oleh Senior Data Analyst Team 3A*
