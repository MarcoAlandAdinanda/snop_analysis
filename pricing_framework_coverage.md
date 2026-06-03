# Pricing Decision Framework — Coverage Ratio (End_Inv / Firm_Demand)

---

## 1. Definisi

Coverage Ratio = **Ending Inventory / Firm Demand**

Arti: **"Berapa bulan demand bisa dipenuhi dengan inventory yang tersisa di akhir bulan."**

---

## 2. Threshold & Decision

### Decision Tree by Coverage

```
              ┌──────────────────────────────────┐
              │  Coverage = End_Inv / Firm_Demand  │
              └──────────────┬───────────────────┘
                             │
      ┌──────────────────────┼──────────────────────┐
      ▼                      ▼                      ▼
┌──────────────┐     ┌──────────────┐      ┌──────────────┐
│ < 0.3        │     │ 0.3 – 2.5    │      │ > 2.5        │
│ STOCKOUT     │     │ OPTIMAL      │      │ OVERLOAD     │
└──────┬───────┘     └──────┬───────┘      └──────┬───────┘
       │                    │                      │
       ▼                    ▼                      ▼
┌──────────────┐     ┌──────────────┐      ┌──────────────┐
│ NAIKKAN      │     │ TAHAN        │      │ TAHAN price  │
│ Price +5-10% │     │ Price $95-105│      │ $90-100      │
│ ke $105-110  │     │              │      │ STOP produksi│
└──────────────┘     └──────────────┘      └──────────────┘
```

### Tabel Threshold Detail

| Coverage | Status | Price Action | Target Price | Target Margin | Contoh 5B |
|---|---|---|---|---|---|
| **< 0.3** | 🚨 Stockout | **↑ +5% sd +10%** | $105–110 | 50–52% | Bln 8: $100→$110 |
| **0.3–1.0** | ⚠️ Menipis | → Tahan / ↑ tipis | $100–105 | 48–52% | Bln 10: $97→$106 |
| **1.0–2.5** | 🟢 Optimal | → Tahan | $95–105 | 48–50% | Bln 1-6: tahan ✅ |
| **> 2.5** | 🟡 Overload | → Tahan / ↓ tipis | $90–100 | 44–48% | — (jarang terjadi) |
| **ANY** | — | **JANGAN dumping** | **Floor $90** | **≥ 44%** | — |

---

## 3. Validasi dari Data Aktual

### Team 5B (profit $55,122 🥇) — Perilaku Ideal

| Bulan | Coverage | Aksi | Hasil |
|---|---|---|---|
| 5 | 0.54 (menipis) | Tahan $100 | Margin 50%, SL 100% |
| 6 | 0.33 (menipis) | Tahan $100 | Margin 50% |
| 7 | 0.00 (stockout) | Tahan $100 | SL turun ke 73% |
| 8 | **0.00** (stockout) | **↑ NAIK ke $110** | **SL pulih, margin 54.5%** |
| 10 | 0.45 (menipis) | **↑ NAIK ke $106** | Profit tertinggi $7,304 |
| 11 | 0.41 (menipis) | Tahan $106 | Profit $10,222 🥇 |
| 12 | **0.00** (stockout) | **↑ NAIK ke $125** | **Profit $9,725, margin 60%** |

**Pola 5B:** Setiap kali coverage rendah (< 0.3), mereka **menaikkan** price — kebalikan dari respons intuitif.

### Team 3A (profit $44,754 ❌) — Perilaku Salah

| Bulan | Coverage | Aksi | Seharusnya |
|---|---|---|---|
| 7 | **0.00** (stockout) | **↓ TURUN ke $99** | ↑ **Naikkan ke $105-110** |
| 8 | **0.00** (stockout) | Tahan $100 | ↑ **Naikkan ke $105-110** |
| 9 | 0.19 (kritis) | Tahan $100 | ↑ Naikkan tipis |
| 10 | **2.50** (overload) | Tahan $101 | ➡ Tahan, stop produksi |
| 11 | **2.45** (overload) | Tahan $100 | ➡ Tahan, stop produksi ✅ |
| 12 | 0.78 (menipis) | **↓ DUMPING $80** | ➡ **Tahan $95, floor $90** |

**Pola 3A:** Menurunkan price saat stockout (salah besar), dumping saat coverage moderate (salah).

### AI Team (profit $35,132) — Stabil

| Bulan | Coverage | Aksi |
|---|---|---|
| 4 | 0.26 (kritis) | Tahan $100 |
| 7-9 | 0.00 (stockout) | Turunkan gradual $95→$91 |
| 10-12 | > 2.5 (overload) | Turunkan gradual $90→$88 |

AI Team tidak membuat kesalahan besar (tidak dumping), tapi juga tidak agresif menaikkan price. Hasilnya: profit stabil, tidak maksimal.

---

## 4. Insight Kunci

### Kesalahan #1: Coverage rendah — jangan turunkan price

```
Intuisi salah: "Inventory habis, turunkan harga biar pelanggan tetap beli"
Fakta:      Inventory sudah habis, turunkan harga → stockout makin parah
            + margin turun + penalty naik = DOUBLE DAMAGE
Benar:      Naikkan harga → kurangi demand → inventory cukup untuk yang benar-benar beli
            + margin naik + SL pulih = WIN-WIN
```

**Data:** Team 3A turunkan price saat coverage 0.00 (Bln 7) → demand tetap tinggi (135), stockout parah (SL 59.6%), penalty $1,220.

### Kesalahan #2: Coverage overload — jangan dumping

```
Intuisi salah: "Inventory menumpuk, dumping harga untuk clear stock"
Fakta:      Dumping $80 → margin 37.5%, profit $6,610
            Padahal $95 → margin 47%, profit ~$8,500
            Selisih: -$1,890 hanya karena panik
Benar:      Stop produksi + tahan price → inventory turun alami dalam 2-3 bulan
            Tanpa merusak margin
```

**Data:** Bln 11 coverage 2.45 (overload), 3A panik di Bln 12 dan dumping. Bln 10-11 produksi 700 unit (arrival 400+300) — seharusnya dihentikan.

### Kesalahan #3: Coverage moderate — jangan panik

```
Coverage 0.78 (Bln 12) menunjukkan inventory masih cukup untuk ~3 minggu.
BUKAN alasan untuk dumping.

Team 3A panik karena MoC sebelumnya 6.03 (overload parah).
Tapi Coverage 0.78 saat demand 298 unit masih masuk akal.

Keputusan benar: Tahan di $95, biarkan inventory turun ke ~100 unit (coverage ~0.3)
Keputusan 3A: Dumping $80 → inventory turun ke 233 (masih cukup) tapi margin hancur.
```

---

## 5. Aturan Praktis untuk Sales Planner

### Setiap Bulan — Cek Coverage

```
If Ending Inventory == 0:
    → NAIKKAN price (jangan pernah turunkan!)
    
If Coverage < 0.3:
    → NAIKKAN price +5-10%
    → Ini kondisi DARURAT
    
If Coverage 0.3–1.0:
    → TAHAN price atau NAIKKAN tipis
    → Waspada, bisa masuk stockout

If Coverage 1.0–2.5:
    → TAHAN price di $95-105
    → Kondisi IDEAL

If Coverage > 2.5:
    → TAHAN price $90-100
    → STOP produksi
    → JANGAN dumping! Biarkan inventory turun alami
```

### Price Floor

```
Coverage berapa pun:
    Price TIDAK BOLEH < $90
    Margin minimum 44%
    Di bawah $90 = Zona Bahaya
```

---

## 6. Perbandingan: Coverage vs MoC

| Aspek | Coverage (End_Inv / Demand) | MoC |
|---|---|---|
| **Data** | Ending inventory + Firm demand | Pipeline + Forecast |
| **Mudah** | ✅ Langsung dari laporan bulanan | ❌ Butuh perhitungan pipeline + forecast |
| **Akurat** | Mencerminkan kondisi aktual akhir bulan | Mencerminkan proyeksi ke depan |
| **Threshold** | < 0.3 stockout, > 2.5 overload | < 2.0 stockout, > 3.5 overload |
| **Cocok untuk** | **Sales Planner (pricing decisions)** | Production Planner (inventory planning) |

**Kesimpulan:** Coverage Ratio lebih praktis untuk Sales Planner karena data selalu tersedia setiap bulan tanpa perhitungan tambahan. Threshold bisa langsung dipakai untuk menentukan arah price.

---

*Bersumber dari `df_kpi_all_players.csv` — Data Team 3A, Team 5B, AI Team (12 bulan)*
