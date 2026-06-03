#!/usr/bin/env python3
"""Helper script to generate the KPI notebook .ipynb file."""

import json

cells = []

def md(source_lines):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [l + "\n" for l in source_lines]
    })

def code(source_lines):
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [l + "\n" for l in source_lines],
        "outputs": [],
        "execution_count": None
    })

md([
    "# KPI Generation untuk Sales Planner S&OP Simulation",
    "",
    "Notebook ini menghasilkan seluruh atribut/kolom KPI berdasarkan panduan `kpis.md`",
    "menggunakan data historis `df_history_display_all_players.csv`.",
    "",
    "**KPI yang dihasilkan:**",
    "- Revenue Growth, Gross Margin, Operating Profit",
    "- Market Share, MS Momentum, Relative Price Index",
    "- Service Level, Stockout Rate, Fill Rate",
    "- Forecast Accuracy (MAPE), Forecast Bias",
    "- Inventory Turnover, Price Elasticity",
    "- Competitive Pressure Score (CPS), Pricing Power Indicator (PPI)"
])

code([
    "import pandas as pd",
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "import seaborn as sns",
    "import warnings",
    "warnings.filterwarnings('ignore')",
    "",
    "sns.set_style('whitegrid')",
    "plt.rcParams['figure.figsize'] = (14, 6)",
    "plt.rcParams['axes.titlesize'] = 13",
    "plt.rcParams['axes.labelsize'] = 11",
    "",
    "print('✅ Libraries loaded')"
])

code([
    "df = pd.read_csv('../df_history_display_all_players.csv')",
    "df['month'] = df['month'].astype(int)",
    "df = df.sort_values(['team_name', 'month']).reset_index(drop=True)",
    "",
    "print(f'Shape: {df.shape}')",
    "print(f'Teams ({df[\"team_name\"].nunique()}): {df[\"team_name\"].unique().tolist()}')",
    "print(f'Month range: {df[\"month\"].min()} - {df[\"month\"].max()}')",
    "print(f'Columns: {df.columns.tolist()}')",
    "df.head(3)"
])

md([
    "## Section 2 — Feature Engineering (KPI Baru)",
    "",
    "Menghitung seluruh KPI berdasarkan formulasi di `kpis.md`."
])

code([
    "df['unit_cost'] = np.where(",
    "    df['units_sold'] > 0,",
    "    df['cogs_amt'] / df['units_sold'],",
    "    np.nan",
    ")",
    "print('✅ unit_cost computed')"
])

code([
    "df['revenue_growth'] = df.groupby('team_name')['revenue_amt'].pct_change()",
    "df['revenue_growth'] = df['revenue_growth'].replace([np.inf, -np.inf], np.nan)",
    "print('✅ Revenue Growth computed')"
])

code([
    "df['gross_margin'] = (df['revenue_amt'] - df['cogs_amt']) / df['revenue_amt']",
    "print('✅ Gross Margin computed')"
])

code([
    "df['operating_profit'] = (",
    "    df['revenue_amt']",
    "    - df['cogs_amt']",
    "    - df['inventory_holding_amt']",
    "    - df['stockout_penalty_amt']",
    ")",
    "print('✅ Operating Profit computed')"
])

code([
    "df['market_share'] = df['firm_demand'] / df['total_market']",
    "print('✅ Market Share computed')"
])

code([
    "df['ms_momentum'] = df.groupby('team_name')['market_share'].diff()",
    "",
    "df['ms_momentum_3mo'] = (",
    "    df.groupby('team_name')['market_share'].transform(lambda x: x - x.shift(3)) / 3",
    ")",
    "print('✅ MS Momentum (1mo & 3mo rolling) computed')"
])

code([
    "df['rpi'] = (df['price'] - df['competitor_price']) / df['competitor_price']",
    "print('✅ Relative Price Index computed')"
])

code([
    "df['missed_demand'] = (df['firm_demand'] - df['units_sold']).clip(lower=0)",
    "",
    "df['stockout_rate'] = np.where(",
    "    df['firm_demand'] > 0,",
    "    df['missed_demand'] / df['firm_demand'],",
    "    np.nan",
    ")",
    "",
    "df['fill_rate'] = np.where(",
    "    df['firm_demand'] > 0,",
    "    df['units_sold'] / df['firm_demand'],",
    "    np.nan",
    ")",
    "print('✅ Missed Demand, Stockout Rate, Fill Rate computed')"
])

code([
    "df['ape'] = np.where(",
    "    df['firm_demand'] > 0,",
    "    (df['forecast_error'].abs() / df['firm_demand']),",
    "    np.nan",
    ")",
    "",
    "df['forecast_accuracy'] = 1 - df['ape']",
    "",
    "mape_per_team = df.groupby('team_name')['ape'].mean().reset_index()",
    "mape_per_team.columns = ['team_name', 'mape']",
    "mape_per_team['forecast_accuracy_avg'] = 1 - mape_per_team['mape']",
    "",
    "bias_per_team = df.groupby('team_name')['forecast_error'].mean().reset_index()",
    "bias_per_team.columns = ['team_name', 'forecast_bias']",
    "",
    "df = df.merge(mape_per_team[['team_name', 'mape', 'forecast_accuracy_avg']], on='team_name')",
    "df = df.merge(bias_per_team, on='team_name')",
    "",
    "print('✅ Forecast Accuracy (MAPE) and Forecast Bias computed')"
])

code([
    "df['avg_inventory'] = (df['beginning_inventory'] + df['ending_inventory']) / 2",
    "",
    "df['inventory_turnover'] = np.where(",
    "    df['avg_inventory'] > 0,",
    "    df['cogs_amt'] / df['avg_inventory'],",
    "    np.nan",
    ")",
    "",
    "df['inventory_turnover_annualized'] = df['inventory_turnover'] * 12",
    "print('✅ Inventory Turnover computed')"
])

code([
    "pct_demand = df.groupby('team_name')['firm_demand'].pct_change()",
    "pct_price = df.groupby('team_name')['price'].pct_change()",
    "",
    "df['price_elasticity'] = np.where(",
    "    (pct_price != 0) & pct_price.notna() & pct_demand.notna(),",
    "    pct_demand / pct_price,",
    "    np.nan",
    ")",
    "df['price_elasticity'] = df['price_elasticity'].replace([np.inf, -np.inf], np.nan)",
    "print('✅ Price Elasticity computed')"
])

code([
    "df['cps'] = df['rpi'] * (-df['ms_momentum'])",
    "print('✅ Competitive Pressure Score computed')"
])

code([
    "ms_momentum_neg = df['ms_momentum'].clip(upper=0)",
    "",
    "df['ppi'] = np.where(",
    "    (1 + ms_momentum_neg.abs()) != 0,",
    "    (df['gross_margin'] * df['service_level']) / (1 + ms_momentum_neg.abs()),",
    "    np.nan",
    ")",
    "print('✅ Pricing Power Indicator computed')"
])

md([
    "### Preview Data dengan Semua KPI"
])

code([
    "kpi_cols = [",
    "    'team_name', 'month',",
    "    'revenue_amt', 'revenue_growth',",
    "    'gross_margin', 'operating_profit',",
    "    'market_share', 'ms_momentum', 'ms_momentum_3mo',",
    "    'rpi',",
    "    'service_level', 'stockout_rate', 'fill_rate',",
    "    'missed_demand',",
    "    'forecast_accuracy', 'forecast_accuracy_avg', 'forecast_bias',",
    "    'months_of_cover', 'inventory_turnover', 'inventory_turnover_annualized',",
    "    'price_elasticity',",
    "    'cps', 'ppi',",
    "]",
    "",
    "df_kpi = df[kpi_cols].copy()",
    "display(df_kpi.head(10))",
    "print(f'\\nTotal rows: {len(df_kpi)}')"
])

code([
    "null_counts = df_kpi.isnull().sum()",
    "null_counts[null_counts > 0]"
])

md([
    "## Section 3 — Aggregate KPI per Team"
])

code([
    "summary = df.groupby('team_name').agg({",
    "    'revenue_amt': 'sum',",
    "    'operating_profit': 'sum',",
    "    'gross_margin': 'mean',",
    "    'service_level': 'mean',",
    "    'stockout_rate': 'mean',",
    "    'revenue_growth': 'mean',",
    "    'market_share': 'mean',",
    "    'rpi': 'mean',",
    "    'mape': 'first',",
    "    'forecast_accuracy_avg': 'first',",
    "    'forecast_bias': 'first',",
    "    'inventory_turnover': 'mean',",
    "    'inventory_turnover_annualized': 'mean',",
    "    'price_elasticity': 'mean',",
    "    'cps': 'mean',",
    "    'ppi': 'mean',",
    "    'months_of_cover': 'mean',",
    "}).reset_index().round(4)",
    "",
    "summary.columns = [",
    "    'team_name',",
    "    'total_revenue',",
    "    'total_profit',",
    "    'avg_gross_margin',",
    "    'avg_service_level',",
    "    'avg_stockout_rate',",
    "    'avg_revenue_growth',",
    "    'avg_market_share',",
    "    'avg_rpi',",
    "    'mape',",
    "    'avg_forecast_accuracy',",
    "    'avg_forecast_bias',",
    "    'avg_inventory_turnover',",
    "    'avg_inv_turnover_annualized',",
    "    'avg_price_elasticity',",
    "    'avg_cps',",
    "    'avg_ppi',",
    "    'avg_months_of_cover',",
    "]",
    "",
    "display(summary)",
    "print(f'\\n✅ Summary table: {summary.shape[0]} teams x {summary.shape[1]} metrics')"
])

md([
    "## Section 4 — Visualizations"
])

md([
    "### 4.1 — Revenue Trend per Team"
])

code([
    "fig, axes = plt.subplots(2, 1, figsize=(16, 10))",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[0].plot(tdf['month'], tdf['revenue_amt'] / 1000, marker='o', label=team, linewidth=1.5)",
    "",
    "axes[0].set_title('Revenue Trend per Team', fontweight='bold')",
    "axes[0].set_xlabel('Month')",
    "axes[0].set_ylabel('Revenue (thousands)')",
    "axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[0].grid(True, alpha=0.3)",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[1].plot(tdf['month'], tdf['operating_profit'] / 1000, marker='s', label=team, linewidth=1.5)",
    "",
    "axes[1].set_title('Operating Profit Trend per Team', fontweight='bold')",
    "axes[1].set_xlabel('Month')",
    "axes[1].set_ylabel('Operating Profit (thousands)')",
    "axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.2 — Gross Margin & Market Share Trend"
])

code([
    "fig, axes = plt.subplots(2, 1, figsize=(16, 10))",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[0].plot(tdf['month'], tdf['gross_margin'], marker='o', label=team, linewidth=1.5)",
    "",
    "axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)",
    "axes[0].set_title('Gross Margin Trend per Team', fontweight='bold')",
    "axes[0].set_xlabel('Month')",
    "axes[0].set_ylabel('Gross Margin')",
    "axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[0].grid(True, alpha=0.3)",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[1].plot(tdf['month'], tdf['market_share'], marker='s', label=team, linewidth=1.5)",
    "",
    "axes[1].set_title('Market Share Trend per Team', fontweight='bold')",
    "axes[1].set_xlabel('Month')",
    "axes[1].set_ylabel('Market Share')",
    "axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.3 — Service Level & Stockout Rate"
])

code([
    "fig, axes = plt.subplots(2, 1, figsize=(16, 10))",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[0].plot(tdf['month'], tdf['service_level'], marker='o', label=team, linewidth=1.5)",
    "",
    "axes[0].axhline(y=1.0, color='green', linestyle='--', alpha=0.4, label='Perfect SL')",
    "axes[0].set_title('Service Level Trend per Team', fontweight='bold')",
    "axes[0].set_xlabel('Month')",
    "axes[0].set_ylabel('Service Level')",
    "axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[0].grid(True, alpha=0.3)",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[1].plot(tdf['month'], tdf['stockout_rate'], marker='s', label=team, linewidth=1.5)",
    "",
    "axes[1].set_title('Stockout Rate Trend per Team', fontweight='bold')",
    "axes[1].set_xlabel('Month')",
    "axes[1].set_ylabel('Stockout Rate')",
    "axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.4 — Correlation Heatmap Antar KPI"
])

code([
    "kpi_corr_cols = [",
    "    'revenue_growth', 'gross_margin', 'operating_profit',",
    "    'market_share', 'ms_momentum', 'rpi',",
    "    'service_level', 'stockout_rate',",
    "    'forecast_accuracy', 'mape',",
    "    'inventory_turnover', 'months_of_cover',",
    "    'price_elasticity', 'cps', 'ppi',",
    "]",
    "",
    "corr_df = df[kpi_corr_cols].dropna()",
    "corr_matrix = corr_df.corr()",
    "",
    "plt.figure(figsize=(14, 10))",
    "mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)",
    "sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',",
    "            center=0, vmin=-1, vmax=1, linewidths=0.5)",
    "plt.title('Correlation Matrix — All KPI Variables', fontweight='bold', fontsize=14)",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.5 — Forecast Accuracy & Bias per Team (Bar Chart)"
])

code([
    "fig, axes = plt.subplots(1, 2, figsize=(16, 6))",
    "",
    "colors_acc = plt.cm.Blues(np.linspace(0.4, 0.9, len(summary)))",
    "axes[0].barh(summary['team_name'], summary['avg_forecast_accuracy'], color=colors_acc)",
    "axes[0].axvline(x=0.8, color='red', linestyle='--', alpha=0.6, label='80% threshold')",
    "axes[0].set_xlabel('Avg Forecast Accuracy')",
    "axes[0].set_title('Forecast Accuracy per Team (1 - MAPE)', fontweight='bold')",
    "axes[0].legend()",
    "axes[0].grid(True, alpha=0.3, axis='x')",
    "",
    "colors_bias = plt.cm.PiYG(np.linspace(0.2, 0.8, len(summary)))",
    "bars = axes[1].barh(summary['team_name'], summary['avg_forecast_bias'], color=colors_bias)",
    "axes[1].axvline(x=0, color='black', linestyle='-', alpha=0.5)",
    "axes[1].set_xlabel('Avg Forecast Bias')",
    "axes[1].set_title('Forecast Bias per Team (positive = underforecast)', fontweight='bold')",
    "axes[1].grid(True, alpha=0.3, axis='x')",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.6 — Price vs Market Share Scatter"
])

code([
    "plt.figure(figsize=(14, 7))",
    "",
    "teams = df['team_name'].unique()",
    "colors = plt.cm.tab10(np.linspace(0, 1, len(teams)))",
    "",
    "for team, color in zip(teams, colors):",
    "    tdf = df[df['team_name'] == team]",
    "    plt.scatter(tdf['price'], tdf['market_share'] * 100,",
    "                s=60, label=team, color=color, alpha=0.7, edgecolors='k', linewidth=0.5)",
    "",
    "plt.xlabel('Selling Price')",
    "plt.ylabel('Market Share (%)')",
    "plt.title('Price vs Market Share — All Teams & Months', fontweight='bold')",
    "plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "plt.grid(True, alpha=0.3)",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.7 — Competitive Pressure & Pricing Power"
])

code([
    "fig, axes = plt.subplots(1, 2, figsize=(16, 6))",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[0].plot(tdf['month'], tdf['cps'], marker='o', label=team, linewidth=1.5)",
    "",
    "axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)",
    "axes[0].set_title('Competitive Pressure Score (CPS)', fontweight='bold')",
    "axes[0].set_xlabel('Month')",
    "axes[0].set_ylabel('CPS')",
    "axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[0].grid(True, alpha=0.3)",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[1].plot(tdf['month'], tdf['ppi'], marker='s', label=team, linewidth=1.5)",
    "",
    "axes[1].set_title('Pricing Power Indicator (PPI)', fontweight='bold')",
    "axes[1].set_xlabel('Month')",
    "axes[1].set_ylabel('PPI')",
    "axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "### 4.8 — Inventory Turnover & Months of Coverage"
])

code([
    "fig, axes = plt.subplots(2, 1, figsize=(16, 10))",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[0].plot(tdf['month'], tdf['inventory_turnover_annualized'], marker='o', label=team, linewidth=1.5)",
    "",
    "axes[0].set_title('Inventory Turnover (Annualized) per Team', fontweight='bold')",
    "axes[0].set_xlabel('Month')",
    "axes[0].set_ylabel('Turnover (annualized)')",
    "axes[0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[0].grid(True, alpha=0.3)",
    "",
    "for team in df['team_name'].unique():",
    "    tdf = df[df['team_name'] == team]",
    "    axes[1].plot(tdf['month'], tdf['months_of_cover'], marker='s', label=team, linewidth=1.5)",
    "",
    "axes[1].axhline(y=3, color='green', linestyle='--', alpha=0.4, label='3mo target')",
    "axes[1].set_title('Months of Coverage per Team', fontweight='bold')",
    "axes[1].set_xlabel('Month')",
    "axes[1].set_ylabel('Months of Cover')",
    "axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')",
    "axes[1].grid(True, alpha=0.3)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

md([
    "## Section 5 — Export",
    "",
    "Menyimpan enriched dataframe dan summary ke CSV."
])

code([
    "output_path = '../df_kpi_all_players.csv'",
    "df.to_csv(output_path, index=False)",
    "print(f'✅ Enriched dataframe saved: {output_path} ({df.shape[0]} rows x {df.shape[1]} cols)')"
])

code([
    "summary_path = '../df_kpi_summary.csv'",
    "summary.to_csv(summary_path, index=False)",
    "print(f'✅ Summary saved: {summary_path} ({summary.shape[0]} teams x {summary.shape[1]} metrics)')"
])

md([
    "---",
    "**Notebook selesai.** Semua KPI per panduan `kpis.md` telah dihasilkan."
])

# Build notebook JSON
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

with open('01_generate_kpi.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("OK - Notebook created: 01_generate_kpi.ipynb")
