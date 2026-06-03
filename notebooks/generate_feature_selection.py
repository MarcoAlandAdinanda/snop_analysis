#!/usr/bin/env python3
"""Generate 02_feature_selection.ipynb — Feature Selection for Sales Planner."""

import json

cells = []

def md(source):
    cells.append({
        "cell_type": "markdown", "metadata": {},
        "source": [l + "\n" for l in source]
    })

def code(source):
    cells.append({
        "cell_type": "code", "metadata": {},
        "source": [l + "\n" for l in source],
        "outputs": [], "execution_count": None
    })

# ============================================================
# SECTION 1 — Setup & Load
# ============================================================

md([
    "# Feature Selection untuk Sales Planner (Pricing Decision)",
    "",
    "Tujuan: Menentukan variabel non-KPI mana yang paling berkorelasi dengan",
    "KPI-KPI yang relevan untuk Sales Planner dalam menentukan harga.",
    "",
    "## Alur",
    "1. Pisahkan kolom menjadi **KPI** (dari `kpis.md`) dan **Non-KPI** (original data)",
    "2. Pilih 9 KPI yang relevan untuk Sales Planner (domain knowledge)",
    "3. Analisis korelasi setiap selected KPI vs seluruh non-KPI variables",
    "4. Composite scoring & ranking fitur (elbow method)",
    "5. Validasi dengan Random Forest (RMSE comparison)",
    "6. Rekomendasi fitur final"
])

code([
    "import pandas as pd",
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "import seaborn as sns",
    "from sklearn.feature_selection import mutual_info_regression",
    "from sklearn.ensemble import RandomForestRegressor",
    "from sklearn.model_selection import cross_val_score, GroupKFold",
    "from sklearn.preprocessing import StandardScaler",
    "from sklearn.metrics import make_scorer, mean_squared_error",
    "import warnings",
    "warnings.filterwarnings('ignore')",
    "",
    "sns.set_style('whitegrid')",
    "plt.rcParams['figure.figsize'] = (14, 6)",
    "plt.rcParams['axes.titlesize'] = 13",
    "plt.rcParams['axes.labelsize'] = 11",
    "",
    "print('OK Libraries loaded')"
])

code([
    "df = pd.read_csv('../df_kpi_all_players.csv')",
    "df = df.sort_values(['team_name', 'month']).reset_index(drop=True)",
    "print(f'Shape: {df.shape}')",
    "print(f'Columns ({len(df.columns)}): {df.columns.tolist()}')"
])

# ============================================================
# SECTION 2 — Separate KPI vs Non-KPI
# ============================================================

md([
    "## Section 2 — Definisi KPI vs Non-KPI",
    "",
    "Berdasarkan panduan `kpis.md`, kolom dikelompokkan menjadi:",
    "- **KPI columns**: metrik-metrik yang didefinisikan sebagai KPI",
    "- **Non-KPI columns**: data original + derived variables yang bukan KPI"
])

code([
    "kpi_columns = [",
    "    'revenue_amt', 'revenue_growth',",
    "    'gross_margin', 'operating_profit',",
    "    'market_share', 'ms_momentum', 'ms_momentum_3mo',",
    "    'rpi',",
    "    'service_level', 'fill_rate', 'stockout_rate', 'missed_demand',",
    "    'forecast_error', 'forecast_accuracy', 'mape',",
    "    'forecast_accuracy_avg', 'forecast_bias',",
    "    'months_of_cover', 'pipeline_units',",
    "    'inventory_turnover', 'inventory_turnover_annualized',",
    "    'price_elasticity', 'cps', 'ppi',",
    "]",
    "",
    "non_kpi_columns = [",
    "    'total_market', 'competitor_demand', 'firm_demand',",
    "    'competitor_price',",
    "    'beginning_inventory', 'arrival_qty', 'units_sold',",
    "    'ending_inventory', 'in_transit', 'production_order',",
    "    'forecast_made',",
    "    'price', 'ai_price',",
    "    'ai_forecast_qty', 'ai_production_order',",
    "    'cogs_amt', 'inventory_holding_amt', 'stockout_penalty_amt',",
    "    'unit_cost', 'avg_inventory',",
    "]",
    "",
    "print(f'KPI columns ({len(kpi_columns)}): {kpi_columns}')",
    "print(f'Non-KPI columns ({len(non_kpi_columns)}): {non_kpi_columns}')",
    "",
    "# verify no overlap",
    "overlap = set(kpi_columns) & set(non_kpi_columns)",
    "print(f'Overlap: {overlap if overlap else \"None\"}')",
    "",
    "# verify all columns accounted for",
    "id_cols = ['team_name', 'team_id', 'month']",
    "all_accounted = id_cols + kpi_columns + non_kpi_columns",
    "missing = [c for c in df.columns if c not in all_accounted]",
    "print(f'Missing from grouping: {missing if missing else \"None\"}')"
])

# ============================================================
# SECTION 3 — Select KPIs for Sales Planner
# ============================================================

md([
    "## Section 3 — Seleksi KPI Sales Planner (Domain Knowledge)",
    "",
    "Dari seluruh KPI, dipilih 9 yang paling relevan untuk Sales Planner",
    "dalam menentukan harga, berdasarkan panduan `kpis.md`:",
    "",
    "| # | KPI | Kategori | Alasan Relevansi |",
    "|---|-----|----------|-----------------|",
    "| 1 | `revenue_growth` | Growth | Target utama pricing — harga memengaruhi pertumbuhan revenue |",
    "| 2 | `gross_margin` | Profitability | = (P - Cost)/P, fungsi langsung dari price |",
    "| 3 | `operating_profit` | Profitability | Profit akhir setelah biaya — tujuan bisnis |",
    "| 4 | `market_share` | Competitive | Harga menentukan posisi kompetitif |",
    "| 5 | `rpi` | Competitive | Posisi harga relatif ke kompetitor |",
    "| 6 | `service_level` | Operational Constraint | Harga tinggi → demand turun → SL naik (inventory cukup); price rendah → demand naik → SL turun (stockout) |",
    "| 7 | `price_elasticity` | Strategic Pricing | Sensitivitas demand terhadap price |",
    "| 8 | `ppi` | Strategic Pricing | Kemampuan menaikkan harga tanpa kehilangan pangsa pasar |",
    "| 9 | `cps` | Strategic Pricing | Tekanan kompetitif pada pricing |"
])

code([
    "selected_kpis = [",
    "    'revenue_growth',",
    "    'gross_margin',",
    "    'operating_profit',",
    "    'market_share',",
    "    'rpi',",
    "    'service_level',",
    "    'price_elasticity',",
    "    'ppi',",
    "    'cps',",
    "]",
    "",
    "print(f'Selected KPIs for Sales Planner ({len(selected_kpis)}):')",
    "for i, k in enumerate(selected_kpis, 1):",
    "    print(f'  {i}. {k}')"
])

# ============================================================
# SECTION 4 — Clean Data
# ============================================================

md([
    "## Section 4 — Data Cleaning",
    "",
    "Menangani missing values, infinite values, dan memastikan data siap",
    "untuk analisis korelasi."
])

code([
    "analyze_df = df[id_cols + selected_kpis + non_kpi_columns].copy()",
    "",
    "# Replace inf dengan NaN",
    "numeric_cols = selected_kpis + non_kpi_columns",
    "analyze_df[numeric_cols] = analyze_df[numeric_cols].replace([np.inf, -np.inf], np.nan)",
    "",
    "# Drop rows dengan NaN pada selected KPIs atau non-KPI",
    "before = len(analyze_df)",
    "analyze_df = analyze_df.dropna(subset=numeric_cols)",
    "after = len(analyze_df)",
    "print(f'Rows dropped due to NaN: {before - after}')",
    "print(f'Remaining rows: {after}')",
    "print(f'Unique teams: {analyze_df[\"team_name\"].nunique()}')",
    "print(f'Month range: {analyze_df[\"month\"].min()} - {analyze_df[\"month\"].max()}')"
])

code([
    "print('Missing values per column:')",
    "missing = analyze_df[numeric_cols].isnull().sum()",
    "print(missing[missing > 0] if any(missing > 0) else '  None')"
])

code([
    "print('Basic statistics of selected KPIs:')",
    "analyze_df[selected_kpis].describe().round(4)"
])

code([
    "print('Basic statistics of non-KPI variables:')",
    "analyze_df[non_kpi_columns].describe().round(4)"
])

# ============================================================
# SECTION 5 — Correlation Analysis
# ============================================================

md([
    "## Section 5 — Korelasi: Selected KPIs vs Non-KPI Variables",
    "",
    "Tiga metode digunakan untuk menangkap berbagai jenis hubungan:",
    "- **Pearson r**: hubungan linear",
    "- **Spearman ρ**: hubungan monotonik (termasuk non-linear monotonik)",
    "- **Mutual Information**: hubungan non-linear umum (tanpa asumsi distribusi)"
])

# 5a: Pearson
md([
    "### 5.1 — Pearson Correlation"
])

code([
    "def pearson_matrix(targets, features, data):",
    "    result = pd.DataFrame(index=targets, columns=features, dtype=float)",
    "    for t in targets:",
    "        for f in features:",
    "            r = data[[t, f]].corr(method='pearson').iloc[0, 1]",
    "            result.loc[t, f] = r if not np.isnan(r) else 0",
    "    return result",
    "",
    "pearson_r = pearson_matrix(selected_kpis, non_kpi_columns, analyze_df)",
    "print('Pearson Correlation: Selected KPIs (rows) vs Non-KPI variables (cols)')",
    "pearson_r"
])

# 5b: Spearman
md([
    "### 5.2 — Spearman Correlation"
])

code([
    "def spearman_matrix(targets, features, data):",
    "    result = pd.DataFrame(index=targets, columns=features, dtype=float)",
    "    for t in targets:",
    "        for f in features:",
    "            rho = data[[t, f]].corr(method='spearman').iloc[0, 1]",
    "            result.loc[t, f] = rho if not np.isnan(rho) else 0",
    "    return result",
    "",
    "spearman_rho = spearman_matrix(selected_kpis, non_kpi_columns, analyze_df)",
    "print('Spearman Correlation: Selected KPIs (rows) vs Non-KPI variables (cols)')",
    "spearman_rho"
])

# 5c: Mutual Information
md([
    "### 5.3 — Mutual Information",
    "",
    "Mutual Information menangkap hubungan non-linear tanpa asumsi distribusi.",
    "Nilai dinormalisasi dengan membagi dengan entropi bersama."
])

code([
    "def mi_matrix(targets, features, data):",
    "    result = pd.DataFrame(index=targets, columns=features, dtype=float)",
    "    X = data[features].values",
    "    for t in targets:",
    "        y = data[t].values",
    "        mi = mutual_info_regression(X, y, random_state=42)",
    "        result.loc[t, :] = mi",
    "    return result",
    "",
    "mi_scores = mi_matrix(selected_kpis, non_kpi_columns, analyze_df)",
    "print('Mutual Information scores:')",
    "mi_scores.round(4)"
])

# ============================================================
# SECTION 6 — Composite Score
# ============================================================

md([
    "## Section 6 — Composite Score & Ranking",
    "",
    "Composite score menggabungkan ketiga metode:",
    "",
    "1. **Normalisasi** setiap matriks ke [0, 1] (min-max scaling)",
    "2. **Average** across all 9 KPIs untuk setiap non-KPI variable",
    "3. **Rata-rata** dari 3 metode untuk composite final",
    "",
    "Sehingga setiap non-KPI variable mendapat satu skor yang merepresentasikan",
    "seberapa kuat hubungannya dengan KPIs Sales Planner secara keseluruhan."
])

code([
    "def minmax_normalize(df):",
    "    return (df - df.min().min()) / (df.max().max() - df.min().min())",
    "",
    "# 1. Absolute values (kita peduli strength, bukan arah)",
    "pearson_abs = pearson_r.abs()",
    "spearman_abs = spearman_rho.abs()",
    "",
    "# 2. Normalize each matrix to [0, 1]",
    "pearson_norm = minmax_normalize(pearson_abs)",
    "spearman_norm = minmax_normalize(spearman_abs)",
    "mi_norm = minmax_normalize(mi_scores)",
    "",
    "# 3. Average across all 9 KPIs untuk setiap non-KPI variable",
    "composite_per_method = pd.DataFrame({",
    "    'pearson': pearson_norm.mean(axis=0),",
    "    'spearman': spearman_norm.mean(axis=0),",
    "    'mutual_info': mi_norm.mean(axis=0),",
    "})",
    "",
    "# 4. Final composite = mean of 3 methods",
    "composite_per_method['composite'] = composite_per_method.mean(axis=1)",
    "composite_per_method = composite_per_method.sort_values('composite', ascending=False)",
    "",
    "print('Composite Score per Non-KPI Variable (ranked):')",
    "composite_per_method.round(4)"
])

# ============================================================
# SECTION 7 — Elbow Method
# ============================================================

md([
    "## Section 7 — Elbow Method untuk Adaptive Feature Count",
    "",
    "Menentukan jumlah fitur optimal secara adaptif dengan mendeteksi",
    "titik elbow pada kurva marginal gain dari composite score."
])

code([
    "scores = composite_per_method['composite'].values",
    "n = len(scores)",
    "",
    "# Compute marginal gain (difference between consecutive scores)",
    "marginal_gains = np.diff(scores)",
    "",
    "# Find elbow: point where gain drops below threshold",
    "# threshold = mean of gains / 2 (heuristic)",
    "mean_gain = marginal_gains.mean()",
    "threshold = mean_gain / 2",
    "",
    "elbow_idx = None",
    "for i, gain in enumerate(marginal_gains):",
    "    if gain < threshold:",
    "        elbow_idx = i + 1  # +1 because diff reduces length by 1",
    "        break",
    "",
    "if elbow_idx is None:",
    "    elbow_idx = n",
    "",
    "top_n_features = list(composite_per_method.index[:elbow_idx])",
    "",
    "print(f'Marginal gain threshold: {threshold:.4f}')",
    "print(f'Elbow at index: {elbow_idx}')",
    "print(f'Recommended top-{len(top_n_features)} features:')",
    "for i, f in enumerate(top_n_features, 1):",
    "    print(f'  {i}. {f} ({composite_per_method.loc[f, \"composite\"]:.4f})')"
])

# ============================================================
# SECTION 8 — Domain Knowledge Overlay
# ============================================================

md([
    "## Section 8 — Domain Knowledge Overlay",
    "",
    "Beberapa variabel mungkin tidak masuk top-N secara statistik tetapi",
    "secara domain penting untuk Sales Planner. Variabel berikut ditambahkan",
    "ke rekomendasi final jika belum termasuk:",
    "",
    "| Variabel | Alasan Domain |",
    "|----------|---------------|",
    "| `competitor_price` | Harga kompetitor adalah anchor untuk pricing decision |",
    "| `firm_demand` | Volume demand memengaruhi keputusan harga |",
    "| `unit_cost` | Cost dasar menentukan margin minimal |",
    "| `price` | Harga aktual — keputusan utama Sales Planner |",
    "| `cogs_amt` | Total biaya produksi |"
])

code([
    "domain_must_have = [",
    "    'competitor_price',",
    "    'firm_demand',",
    "    'unit_cost',",
    "    'price',",
    "    'cogs_amt',",
    "]",
    "",
    "final_features = list(top_n_features)",
    "added_by_domain = []",
    "for f in domain_must_have:",
    "    if f not in final_features:",
    "        final_features.append(f)",
    "        added_by_domain.append(f)",
    "",
    "# Sort final_features by composite score descending",
    "final_features_sorted = sorted(final_features,",
    "    key=lambda f: composite_per_method.loc[f, 'composite']",
    "    if f in composite_per_method.index else 0,",
    "    reverse=True)",
    "",
    "print(f'Recommended features (statistical): {len(top_n_features)}')",
    "print(f'Added by domain knowledge: {added_by_domain}')",
    "print(f'Final feature set ({len(final_features_sorted)}):')",
    "for i, f in enumerate(final_features_sorted, 1):",
    "    marker = ' [DOMAIN]' if f in added_by_domain else ''",
    "    score = composite_per_method.loc[f, 'composite'] if f in composite_per_method.index else 0",
    "    print(f'  {i:2d}. {f:25s} score={score:.4f}{marker}')"
])

# ============================================================
# SECTION 9 — Validation with Random Forest
# ============================================================

md([
    "## Section 9 — Validasi dengan Random Forest",
    "",
    "Untuk setiap selected KPI, bandingkan 3 konfigurasi:",
    "- **All Features**: semua 20 non-KPI variables",
    "- **Selected Features**: top-N dari elbow method",
    "- **Selected + Domain**: top-N + domain must-have",
    "",
    "Menggunakan 5-fold GroupKFold (group = team_name) untuk menghindari",
    "data leakage antar tim."
])

code([
    "def rmse_cv_rf(X, y, groups, n_folds=5):",
    "    gkf = GroupKFold(n_splits=n_folds)",
    "    rmse_list = []",
    "    for train_idx, val_idx in gkf.split(X, y, groups):",
    "        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]",
    "        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]",
    "        rf = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)",
    "        rf.fit(X_train, y_train)",
    "        y_pred = rf.predict(X_val)",
    "        rmse = np.sqrt(mean_squared_error(y_val, y_pred))",
    "        rmse_list.append(rmse)",
    "    return np.mean(rmse_list), np.std(rmse_list)",
    "",
    "groups = analyze_df['team_name'].values",
    "results = []",
    "",
    "for kpi in selected_kpis:",
    "    y = analyze_df[kpi]",
    "",
    "    # All features",
    "    X_all = analyze_df[non_kpi_columns]",
    "    rmse_mean, rmse_std = rmse_cv_rf(X_all, y, groups)",
    "    results.append({'kpi': kpi, 'config': 'All Features (20)',",
    "                    'rmse_mean': round(rmse_mean, 4), 'rmse_std': round(rmse_std, 4)})",
    "",
    "    # Selected features (top-N from elbow)",
    "    if top_n_features:",
    "        X_sel = analyze_df[top_n_features]",
    "        rmse_mean, rmse_std = rmse_cv_rf(X_sel, y, groups)",
    "        results.append({'kpi': kpi, 'config': f'Selected ({len(top_n_features)})',",
    "                        'rmse_mean': round(rmse_mean, 4), 'rmse_std': round(rmse_std, 4)})",
    "",
    "    # Selected + Domain features",
    "    X_final = analyze_df[final_features]",
    "    rmse_mean, rmse_std = rmse_cv_rf(X_final, y, groups)",
    "    results.append({'kpi': kpi, 'config': f'Final ({len(final_features)})',",
    "                    'rmse_mean': round(rmse_mean, 4), 'rmse_std': round(rmse_std, 4)})",
    "",
    "results_df = pd.DataFrame(results)",
    "print('RMSE Comparison across all selected KPIs:')",
    "results_df.pivot_table(index='kpi', columns='config', values='rmse_mean')"
])

code([
    "# Summary: average RMSE across all KPIs",
    "avg_rmse = results_df.groupby('config')['rmse_mean'].agg(['mean', 'std']).round(4)",
    "avg_rmse.columns = ['avg_rmse', 'std_rmse']",
    "print('Average RMSE across all 9 KPIs:')",
    "avg_rmse"
])

code([
    "# Improvement percentage",
    "all_rmse = results_df[results_df['config'] == 'All Features (20)'].set_index('kpi')['rmse_mean']",
    "final_rmse = results_df[results_df['config'] == f'Final ({len(final_features)})'].set_index('kpi')['rmse_mean']",
    "improv = ((all_rmse - final_rmse) / all_rmse * 100).round(2)",
    "improv_df = pd.DataFrame({",
    "    'all_features_rmse': all_rmse,",
    "    'final_features_rmse': final_rmse,",
    "    'improvement_pct': improv",
    "})",
    "print('\\nImprovement from All Features to Final Features per KPI:')",
    "improv_df"
])

# ============================================================
# SECTION 10 — Visualizations
# ============================================================

md([
    "## Section 10 — Visualizations"
])

md([
    "### 10.1 — Heatmap Pearson Correlation: Selected KPIs vs Non-KPI"
])

code([
    "plt.figure(figsize=(16, 10))",
    "sns.heatmap(pearson_r, annot=True, fmt='.2f', cmap='RdBu_r',",
    "            center=0, vmin=-1, vmax=1, linewidths=0.5, cbar_kws={'shrink': 0.8})",
    "plt.title('Pearson Correlation: Selected KPIs vs Non-KPI Variables',",
    "          fontweight='bold', fontsize=14)",
    "plt.xlabel('Non-KPI Variables', fontsize=12)",
    "plt.ylabel('Selected KPIs (Sales Planner)', fontsize=12)",
    "plt.xticks(rotation=45, ha='right')",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 10.2 — Composite Score Bar Chart dengan Elbow Threshold"
])

code([
    "fig, axes = plt.subplots(1, 2, figsize=(18, 7))",
    "",
    "# Bar chart composite score",
    "colors = ['#2ecc71' if i < elbow_idx else '#95a5a6'",
    "          for i in range(len(composite_per_method))]",
    "axes[0].barh(range(len(composite_per_method)),",
    "             composite_per_method['composite'].values, color=colors)",
    "axes[0].set_yticks(range(len(composite_per_method)))",
    "axes[0].set_yticklabels(composite_per_method.index)",
    "axes[0].axvline(x=composite_per_method['composite'].values[elbow_idx - 1] if elbow_idx > 0 else 0,",
    "                color='red', linestyle='--', alpha=0.7, label=f'Elbow: top-{elbow_idx}')",
    "axes[0].set_xlabel('Composite Score')",
    "axes[0].set_title('Composite Score per Non-KPI Variable', fontweight='bold')",
    "axes[0].legend()",
    "axes[0].grid(True, alpha=0.3, axis='x')",
    "",
    "# Elbow curve",
    "axes[1].plot(range(1, n + 1), scores, 'bo-', linewidth=2, markersize=6)",
    "axes[1].axvline(x=elbow_idx, color='red', linestyle='--',",
    "                alpha=0.7, label=f'Elbow at index {elbow_idx}')",
    "axes[1].set_xlabel('Feature Rank')",
    "axes[1].set_ylabel('Composite Score')",
    "axes[1].set_title('Elbow Curve — Marginal Gain of Composite Score', fontweight='bold')",
    "axes[1].legend()",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 10.3 — RMSE Comparison per KPI"
])

code([
    "fig, ax = plt.subplots(figsize=(16, 7))",
    "",
    "pivot = results_df.pivot_table(index='kpi', columns='config', values='rmse_mean')",
    "pivot.plot(kind='bar', ax=ax, width=0.75, edgecolor='black', linewidth=0.5)",
    "",
    "ax.set_xlabel('Selected KPI', fontsize=12)",
    "ax.set_ylabel('RMSE (5-fold CV)', fontsize=12)",
    "ax.set_title('RMSE Comparison: All Features vs Selected vs Final', fontweight='bold', fontsize=14)",
    "ax.legend(title='Feature Config', bbox_to_anchor=(1.05, 1), loc='upper left')",
    "ax.grid(True, alpha=0.3, axis='y')",
    "ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 10.4 — Scatter Matrix: Top-4 Non-KPI vs Selected KPIs"
])

code([
    "top4 = list(composite_per_method.index[:4])",
    "scatter_cols = top4 + selected_kpis[:4]",
    "",
    "sns.pairplot(analyze_df[scatter_cols].dropna(),",
    "             diag_kind='kde', plot_kws={'alpha': 0.5, 's': 30})",
    "plt.suptitle('Scatter Matrix: Top-4 Non-KPI vs Top-4 Selected KPIs',",
    "             fontweight='bold', fontsize=14, y=1.02)",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 10.5 — Network Graph: KPI-NonKPI Relationships"
])

code([
    "import matplotlib.patches as mpatches",
    "",
    "fig, ax = plt.subplots(figsize=(16, 12))",
    "",
    "threshold = 0.3  # minimum |r| to show edge",
    "",
    "# Positions using circular layout for KPIs and non-KPIs",
    "n_kpi = len(selected_kpis)",
    "n_non = len(non_kpi_columns)",
    "",
    "kpi_angles = np.linspace(0, 2*np.pi, n_kpi, endpoint=False)",
    "non_angles = np.linspace(0, 2*np.pi, n_non, endpoint=False) + np.pi/n_non",
    "",
    "kpi_pos = {k: (np.cos(a), np.sin(a)) for k, a in zip(selected_kpis, kpi_angles)}",
    "non_pos = {k: (np.cos(a)*0.6, np.sin(a)*0.6) for k, a in zip(non_kpi_columns, non_angles)}",
    "",
    "# Draw edges",
    "for kpi in selected_kpis:",
    "    for nk in non_kpi_columns:",
    "        r = pearson_r.loc[kpi, nk]",
    "        if abs(r) >= threshold:",
    "            color = '#e74c3c' if r > 0 else '#3498db'",
    "            width = abs(r) * 3",
    "            ax.plot([kpi_pos[kpi][0], non_pos[nk][0]],",
    "                    [kpi_pos[kpi][1], non_pos[nk][1]],",
    "                    color=color, linewidth=width, alpha=0.4)",
    "",
    "# Draw nodes",
    "for kpi, pos in kpi_pos.items():",
    "    ax.scatter(*pos, s=600, c='#2ecc71', edgecolors='white', linewidth=2, zorder=5)",
    "    ax.annotate(kpi, pos, ha='center', va='center', fontsize=8, fontweight='bold', color='white')",
    "",
    "for nk, pos in non_pos.items():",
    "    ax.scatter(*pos, s=400, c='#f39c12', edgecolors='white', linewidth=2, zorder=5)",
    "    ax.annotate(nk, pos, ha='center', va='center', fontsize=7, color='white')",
    "",
    "ax.set_xlim(-1.3, 1.3)",
    "ax.set_ylim(-1.3, 1.3)",
    "ax.set_aspect('equal')",
    "ax.axis('off')",
    "",
    "legend_elements = [",
    "    mpatches.Patch(color='#2ecc71', label='Selected KPI'),",
    "    mpatches.Patch(color='#f39c12', label='Non-KPI Variable'),",
    "    plt.Line2D([0], [0], color='#e74c3c', linewidth=2, label='Positive correlation'),",
    "    plt.Line2D([0], [0], color='#3498db', linewidth=2, label='Negative correlation'),",
    "]",
    "ax.legend(handles=legend_elements, loc='upper right', fontsize=10)",
    "ax.set_title('Network Graph: KPI-NonKPI Relationships (|r| >= 0.3)',",
    "             fontweight='bold', fontsize=14)",
    "plt.tight_layout()",
    "plt.show()"
])

# ============================================================
# SECTION 11 — Summary & Export
# ============================================================

md([
    "## Section 11 — Summary & Export"
])

code([
    "print('=' * 70)",
    "print('   FEATURE SELECTION SUMMARY — SALES PLANNER')",
    "print('=' * 70)",
    "print()",
    "print(f'Dataset: {len(analyze_df)} rows across {analyze_df[\"team_name\"].nunique()} teams')",
    "print(f'Selected KPIs: {len(selected_kpis)}')",
    "print(f'Non-KPI candidates: {len(non_kpi_columns)}')",
    "print(f'Top-N (elbow): {len(top_n_features)} features')",
    "print(f'Final recommendation: {len(final_features_sorted)} features')",
    "print()",
    "print('Final Feature Ranking (sorted by composite score):')",
    "print('-' * 70)",
    "for i, f in enumerate(final_features_sorted, 1):",
    "    method = 'statistical' if f in top_n_features else 'domain'",
    "    score = composite_per_method.loc[f, 'composite'] if f in composite_per_method.index else '-'",
    "    print(f'  {i:2d}. {f:25s} | score: {score:<8} | source: {method}')",
    "print()",
    "print('RMSE Validation (avg across 9 KPIs):')",
    "print('-' * 70)",
    "for _, row in avg_rmse.iterrows():",
    "    print(f'  {row.name:30s} | RMSE: {row[\"avg_rmse\"]:.4f} +/- {row[\"std_rmse\"]:.4f}')",
])

code([
    "# Export recommendation table (sorted by composite score)",
    "rec_df = pd.DataFrame({",
    "    'rank': range(1, len(final_features_sorted) + 1),",
    "    'feature': final_features_sorted,",
    "    'composite_score': [",
    "        round(composite_per_method.loc[f, 'composite'], 4)",
    "        if f in composite_per_method.index else None",
    "        for f in final_features_sorted",
    "    ],",
    "    'pearson_avg_abs_r': [",
    "        round(pearson_abs[f].mean(), 4)",
    "        if f in pearson_abs.columns else None",
    "        for f in final_features_sorted",
    "    ],",
    "    'spearman_avg_abs_rho': [",
    "        round(spearman_abs[f].mean(), 4)",
    "        if f in spearman_abs.columns else None",
    "        for f in final_features_sorted",
    "    ],",
    "    'mi_avg_score': [",
    "        round(mi_scores[f].mean(), 4)",
    "        if f in mi_scores.columns else None",
    "        for f in final_features_sorted",
    "    ],",
    "    'source': [",
    "        'elbow' if f in top_n_features else 'domain'",
    "        for f in final_features_sorted",
    "    ],",
    "})",
    "",
    "rec_path = '../df_feature_selection_recommendation.csv'",
    "rec_df.to_csv(rec_path, index=False)",
    "print(f'Recommendation table saved: {rec_path}')",
    "print()",
    "rec_df"
])

code([
    "# Export RMSE comparison",
    "rmse_path = '../df_feature_selection_rmse.csv'",
    "results_df.to_csv(rmse_path, index=False)",
    "print(f'RMSE results saved: {rmse_path}')"
])

md([
    "---",
    "**Notebook selesai.** Rekomendasi fitur untuk Sales Planner telah dihasilkan",
    "berdasarkan kombinasi analisis statistik (Pearson, Spearman, Mutual Information)",
    "dan domain knowledge dari panduan `kpis.md`."
])

# ============================================================
# Build notebook JSON
# ============================================================

notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

output_path = '02_feature_selection.ipynb'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"OK - Notebook created: {output_path}")
