#!/usr/bin/env python3
"""Slide 2 — Price vs Months of Cover (MoC): Team 3A vs Team 5B"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 11

df = pd.read_csv('df_kpi_all_players.csv')
df = df[df['team_name'].isin(['Team 3A', 'Team 5B'])].copy()
df = df[df['month'].between(1, 12)]

team3a = df[df['team_name'] == 'Team 3A'].sort_values('month')
team5b = df[df['team_name'] == 'Team 5B'].sort_values('month')

months = list(range(1, 13))
p3 = team3a['price'].values
m3 = team3a['months_of_cover'].values
s3 = team3a['service_level'].values
p5 = team5b['price'].values
m5 = team5b['months_of_cover'].values
s5 = team5b['service_level'].values

fig = plt.figure(figsize=(16, 8.5))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

ax2.axhspan(0, 2.0, facecolor='#ffcccc', alpha=0.20, zorder=0)
ax2.axhspan(2.0, 3.5, facecolor='#ccffcc', alpha=0.20, zorder=0)
ax2.axhspan(3.5, 7.5, facecolor='#fff3cc', alpha=0.20, zorder=0)

ax2.axhline(y=2.0, color='#cc0000', linestyle='--', linewidth=0.9, alpha=0.45)
ax2.axhline(y=3.5, color='#cc6600', linestyle='--', linewidth=0.9, alpha=0.45)

ax1.plot(months, p3, color='#1f77b4', linewidth=2.8, marker='o', markersize=8,
         label='Team 3A — Price', zorder=5)
ax1.plot(months, p5, color='#d62728', linewidth=2.8, marker='s', markersize=8,
         label='Team 5B — Price', zorder=5)

ax2.plot(months, m3, color='#1f77b4', linewidth=1.5, linestyle='--', marker='o',
         markersize=6, alpha=0.55, label='Team 3A — MoC', zorder=4)
ax2.plot(months, m5, color='#d62728', linewidth=1.5, linestyle='--', marker='s',
         markersize=6, alpha=0.55, label='Team 5B — MoC', zorder=4)

ax1.set_xlabel('Month', fontsize=13, fontweight='bold', labelpad=8)
ax1.set_ylabel('Price ($)', fontsize=13, fontweight='bold', color='#333333')
ax2.set_ylabel('Months of Cover (MoC)', fontsize=13, fontweight='bold', color='#333333')

ax1.set_xticks(months)
ax1.tick_params(axis='y', labelsize=11)
ax2.tick_params(axis='y', labelsize=11)
ax1.tick_params(axis='x', labelsize=11)
ax1.set_xlim(0.5, 12.5)
ax1.set_ylim(70, 135)
ax2.set_ylim(0, 7.5)

s = 8.5
ax2.text(11.7, 1.1, 'Stockout Risk\nMoC < 2.0', fontsize=s, color='#cc0000',
         fontweight='bold', va='center', ha='left',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cc0000', alpha=0.7))
ax2.text(11.7, 2.8, 'Optimal Zone\nMoC 2.0\u20133.5', fontsize=s, color='#006600',
         fontweight='bold', va='center', ha='left',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#006600', alpha=0.7))
ax2.text(11.7, 5.7, 'Overload\nMoC > 3.5', fontsize=s, color='#cc6600',
         fontweight='bold', va='center', ha='left',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cc6600', alpha=0.7))

leg1 = ax1.legend(loc='upper left', fontsize=10, framealpha=0.9, edgecolor='#cccccc')
leg_moc = ax2.legend(loc='upper right', fontsize=10, framealpha=0.9, edgecolor='#cccccc')
ax2.add_artist(leg_moc)


# ── Zone legend ──────────────────────────────────────────────
legend_elements = [
    mpatches.Patch(facecolor='#ffcccc', alpha=0.5, label='MoC < 2.0  (Stockout Risk)'),
    mpatches.Patch(facecolor='#ccffcc', alpha=0.5, label='MoC 2.0\u20133.5  (Optimal)'),
    mpatches.Patch(facecolor='#fff3cc', alpha=0.5, label='MoC > 3.5  (Overload)'),
]
leg_zone = ax2.legend(handles=legend_elements, loc='lower center', fontsize=9,
                      framealpha=0.88, edgecolor='#bbbbbb', ncol=3,
                      bbox_to_anchor=(0.5, -0.14))
ax2.add_artist(leg_zone)

fig.suptitle(
    'Price vs Inventory (MoC)  \u2014  Team 3A vs Team 5B',
    fontsize=16, fontweight='bold', y=0.976, color='#111111'
)

fig.tight_layout(rect=[0, 0, 1, 0.96])

output_path = 'visualizations/slide2_price_moc_decision.png'
fig.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
print(f'OK  {output_path}')
plt.close()
