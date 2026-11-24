import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Ensure directory
os.makedirs("images", exist_ok=True)
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 1.2

# ----------------------------------------------------------------------
# 1. NumPy Array & Broadcasting Visual Diagram
# ----------------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 4.5), gridspec_kw={'width_ratios': [1, 0.4, 1.2]})
fig.patch.set_facecolor('#f8fafc')

# Matrix A (3x3)
mat_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ax1.set_facecolor('#ffffff')
im1 = ax1.imshow(mat_a, cmap='Blues', aspect='equal')
for i in range(3):
    for j in range(3):
        ax1.text(j, i, str(mat_a[i, j]), ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
ax1.set_title("Matrix A (Shape: 3x3)", fontsize=13, fontweight='bold', color='#0369a1', pad=12)
ax1.set_xticks(range(3))
ax1.set_yticks(range(3))

# Plus sign
ax2.axis('off')
ax2.text(0.5, 0.5, "+\n(Broadcasting)\n+", ha='center', va='center', fontsize=14, fontweight='bold', color='#f43f5e')

# Vector B broadcasted to (3x3)
mat_b = np.array([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
ax3.set_facecolor('#ffffff')
im3 = ax3.imshow(mat_b, cmap='YlGn', aspect='equal')
for i in range(3):
    for j in range(3):
        ax3.text(j, i, str(mat_b[i, j]), ha='center', va='center', fontsize=14, fontweight='bold', color='#166534')
ax3.set_title("Vector B [10, 20, 30] (Broadcasted to 3x3)", fontsize=13, fontweight='bold', color='#166534', pad=12)
ax3.set_xticks(range(3))
ax3.set_yticks(range(3))

plt.suptitle("NumPy Broadcasting: Shape (3, 3) + Shape (1, 3) = Shape (3, 3)", fontsize=15, fontweight='bold', color='#0f172a', y=1.02)
plt.tight_layout()
plt.savefig("images/numpy_broadcasting_diagram.png", dpi=200, bbox_inches='tight')
plt.close()

# ----------------------------------------------------------------------
# 2. Matplotlib Gallery (2x2 Grid)
# ----------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.patch.set_facecolor('#f8fafc')

# Subplot 1: Line Chart
ax = axes[0, 0]
ax.set_facecolor('#ffffff')
x = np.arange(1, 11)
y1 = np.sin(x/2) * 20 + 50
y2 = np.cos(x/2) * 15 + 40
ax.plot(x, y1, color='#0284c7', marker='o', linewidth=2.5, label='Model Alpha')
ax.plot(x, y2, color='#f43f5e', marker='s', linestyle='--', linewidth=2, label='Model Beta')
ax.set_title("A. Line Chart (Trend Analysis)", fontsize=12, fontweight='bold', color='#0f172a')
ax.set_xlabel("Epoch / Time Index")
ax.set_ylabel("Accuracy (%)")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#f8fafc')

# Subplot 2: Bar Chart
ax = axes[0, 1]
ax.set_facecolor('#ffffff')
categories = ['Python', 'SQL', 'R', 'Java', 'C++']
popularity = [92, 85, 68, 74, 62]
colors = ['#0284c7', '#0ea5e9', '#38bdf8', '#94a3b8', '#cbd5e1']
bars = ax.bar(categories, popularity, color=colors, edgecolor='#0f172a', linewidth=0.8, width=0.6)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_title("B. Bar Chart (Categorical Comparison)", fontsize=12, fontweight='bold', color='#0f172a')
ax.set_ylabel("Popularity Index (%)")
ax.set_ylim(0, 105)
ax.grid(axis='y', linestyle=':', alpha=0.6)

# Subplot 3: Histogram
ax = axes[1, 0]
ax.set_facecolor('#ffffff')
np.random.seed(42)
dist_data = np.random.normal(loc=100, scale=15, size=1000)
n, bins, patches = ax.hist(dist_data, bins=25, color='#10b981', edgecolor='#064e3b', alpha=0.8, density=True)
mu, sigma = 100, 15
best_fit = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, best_fit, color='#047857', linewidth=2.5, label='Normal Distribution')
ax.set_title("C. Histogram (Distribution & KDE Density)", fontsize=12, fontweight='bold', color='#0f172a')
ax.set_xlabel("Value Range")
ax.set_ylabel("Probability Density")
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(facecolor='#f8fafc')

# Subplot 4: Scatter Plot
ax = axes[1, 1]
ax.set_facecolor('#ffffff')
n_pts = 100
x_sc = np.random.rand(n_pts) * 100
y_sc = x_sc * 0.8 + np.random.randn(n_pts) * 15
colors_sc = y_sc
scatter = ax.scatter(x_sc, y_sc, c=colors_sc, cmap='plasma', s=60, alpha=0.85, edgecolors='none')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Cluster Intensity", fontsize=9)
ax.set_title("D. Scatter Plot (Correlation & Clusters)", fontsize=12, fontweight='bold', color='#0f172a')
ax.set_xlabel("Feature X")
ax.set_ylabel("Feature Y")
ax.grid(True, linestyle=':', alpha=0.6)

plt.suptitle("Matplotlib Core Charts Gallery (Jupyter Visualizations)", fontsize=15, fontweight='bold', color='#0f172a', y=0.99)
plt.tight_layout()
plt.savefig("images/matplotlib_gallery.png", dpi=200, bbox_inches='tight')
plt.close()

# ----------------------------------------------------------------------
# 3. Candlestick Stock Chart Sample
# ----------------------------------------------------------------------
fig, (ax_main, ax_vol) = plt.subplots(2, 1, figsize=(11, 6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
fig.patch.set_facecolor('#f8fafc')
ax_main.set_facecolor('#ffffff')
ax_vol.set_facecolor('#ffffff')

# Simulated 15 trading days
np.random.seed(101)
days = np.arange(1, 16)
opens = [100 + i*1.2 + np.random.uniform(-2, 2) for i in days]
closes = [op + np.random.uniform(-4, 5) for op in opens]
highs = [max(op, cl) + np.random.uniform(0.5, 3) for op, cl in zip(opens, closes)]
lows = [min(op, cl) - np.random.uniform(0.5, 3) for op, cl in zip(opens, closes)]
volumes = np.random.randint(10000, 50000, size=len(days))

for i in range(len(days)):
    d = days[i]
    op = opens[i]
    cl = closes[i]
    hi = highs[i]
    lo = lows[i]
    color = '#10b981' if cl >= op else '#ef4444'
    ax_main.plot([d, d], [lo, hi], color=color, linewidth=1.5)
    height = abs(cl - op)
    bottom = min(op, cl)
    ax_main.bar(d, height, bottom=bottom, color=color, edgecolor=color, width=0.6, align='center')
    ax_vol.bar(d, volumes[i], color=color, alpha=0.6, width=0.6)

ma5 = [np.mean(closes[max(0, i-4):i+1]) for i in range(len(closes))]
ax_main.plot(days, ma5, color='#0284c7', linewidth=2, label='5-Day Moving Average (MA)')

ax_main.set_title("Financial Candlestick (OHLC) Chart with Volume & Moving Average", fontsize=13, fontweight='bold', color='#0f172a', pad=10)
ax_main.set_ylabel("Stock Price ($)", fontsize=11)
ax_main.grid(True, linestyle=':', alpha=0.6)
ax_main.legend(facecolor='#f8fafc')

ax_vol.set_ylabel("Volume", fontsize=10)
ax_vol.set_xlabel("Trading Day", fontsize=11)
ax_vol.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig("images/candlestick_financial_chart.png", dpi=200, bbox_inches='tight')
plt.close()

# ----------------------------------------------------------------------
# 4. Seaborn Heatmap & Boxplot Illustration
# ----------------------------------------------------------------------
fig, (ax_hm, ax_box) = plt.subplots(1, 2, figsize=(13, 5))
fig.patch.set_facecolor('#f8fafc')
ax_hm.set_facecolor('#ffffff')
ax_box.set_facecolor('#ffffff')

corr_data = np.array([
    [1.00, 0.85, 0.12, -0.65],
    [0.85, 1.00, 0.28, -0.48],
    [0.12, 0.28, 1.00,  0.05],
    [-0.65, -0.48, 0.05, 1.00]
])
features = ['Age', 'Income', 'Credit_Score', 'Debt_Ratio']
im = ax_hm.imshow(corr_data, cmap='coolwarm', vmin=-1, vmax=1)
for i in range(4):
    for j in range(4):
        ax_hm.text(j, i, f"{corr_data[i, j]:.2f}", ha='center', va='center',
                   color='white' if abs(corr_data[i, j]) > 0.5 else 'black', fontweight='bold')
ax_hm.set_xticks(range(4))
ax_hm.set_yticks(range(4))
ax_hm.set_xticklabels(features, fontsize=10, fontweight='bold')
ax_hm.set_yticklabels(features, fontsize=10, fontweight='bold')
ax_hm.set_title("A. Correlation Heatmap (Feature Relationship Matrix)", fontsize=12, fontweight='bold', color='#0f172a', pad=12)
cbar = plt.colorbar(im, ax=ax_hm, fraction=0.046, pad=0.04)
cbar.set_label("Pearson Correlation Coefficient", fontsize=9)

np.random.seed(99)
group_a = np.random.normal(50, 8, 100)
group_b = np.random.normal(65, 12, 100)
group_c = np.random.normal(80, 15, 100)
group_c = np.append(group_c, [125, 130, 32])

box = ax_box.boxplot([group_a, group_b, group_c], patch_artist=True,
                     boxprops=dict(facecolor='#bae6fd', color='#0284c7', linewidth=1.5),
                     whiskerprops=dict(color='#0284c7', linewidth=1.5),
                     capprops=dict(color='#0284c7', linewidth=1.5),
                     medianprops=dict(color='#f43f5e', linewidth=2.5),
                     flierprops=dict(marker='o', markerfacecolor='#ef4444', markersize=7, linestyle='none'))

colors_bp = ['#bae6fd', '#bbf7d0', '#fef08a']
for patch, color in zip(box['boxes'], colors_bp):
    patch.set_facecolor(color)

ax_box.set_xticklabels(['Dept Alpha', 'Dept Beta', 'Dept Gamma'], fontsize=10, fontweight='bold')
ax_box.set_title("B. Boxplot (Five-Number Summary & Outliers)", fontsize=12, fontweight='bold', color='#0f172a', pad=12)
ax_box.set_ylabel("Performance Metric Score", fontsize=10)
ax_box.grid(axis='y', linestyle=':', alpha=0.6)

plt.suptitle("Seaborn Statistical Visualizations: Heatmaps & Boxplots", fontsize=14, fontweight='bold', color='#0f172a', y=1.02)
plt.tight_layout()
plt.savefig("images/seaborn_heatmap_boxplot.png", dpi=200, bbox_inches='tight')
plt.close()

# ----------------------------------------------------------------------
# 5. Pandas DataFrame & Series Anatomy Diagram
# ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 4.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')

# Draw diagram of DataFrame Anatomy
ax.text(0.5, 0.92, "Pandas DataFrame Architecture & Anatomy", ha='center', va='center', fontsize=14, fontweight='bold', color='#0369a1')

# Draw columns box
rect_cols = plt.Rectangle((0.2, 0.65), 0.75, 0.12, facecolor='#e0f2fe', edgecolor='#0284c7', linewidth=1.5)
ax.add_patch(rect_cols)
ax.text(0.57, 0.71, "Columns (Index): ['EmpID', 'Name', 'Department', 'Salary', 'Experience']", ha='center', va='center', fontsize=10, fontweight='bold', color='#0369a1')

# Draw index box
rect_idx = plt.Rectangle((0.05, 0.15), 0.12, 0.45, facecolor='#fef3c7', edgecolor='#f59e0b', linewidth=1.5)
ax.add_patch(rect_idx)
ax.text(0.11, 0.375, "Row Index\n0\n1\n2\n3", ha='center', va='center', fontsize=10, fontweight='bold', color='#92400e', linespacing=1.6)

# Draw data matrix
rect_data = plt.Rectangle((0.2, 0.15), 0.75, 0.45, facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5)
ax.add_patch(rect_data)
ax.text(0.57, 0.375, "2D Data Values Matrix (NumPy ndarray underneath)\n[101, 'Amit',   'IT',       75000, 4]\n[102, 'Priya',  'HR',       62000, 3]\n[103, 'Rohit',  'IT',       80000, 5]\n[104, 'Sneha',  'Finance',  92000, 7]", ha='center', va='center', fontsize=9.5, family='monospace', color='#1e293b', linespacing=1.6)

ax.annotate("Single Column = 1D Pandas Series", xy=(0.35, 0.15), xytext=(0.35, 0.04),
            arrowprops=dict(arrowstyle="->", color='#f43f5e', lw=1.5),
            ha='center', fontsize=10, fontweight='bold', color='#f43f5e')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig("images/pandas_dataframe_anatomy.png", dpi=200, bbox_inches='tight')
plt.close()

# ----------------------------------------------------------------------
# 6. Plotly Interactive UI Simulation Graphic
# ----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')

# Draw simulated Plotly canvas with interactive toolbar & hover card
ax.text(0.5, 0.94, "Plotly Interactive Charting & Web Dashboard Architecture", ha='center', va='center', fontsize=13, fontweight='bold', color='#0f172a')

# Plotly toolbar
rect_bar = plt.Rectangle((0.6, 0.82), 0.36, 0.08, facecolor='#f1f5f9', edgecolor='#94a3b8', linewidth=1, linestyle='--')
ax.add_patch(rect_bar)
ax.text(0.78, 0.86, "ModeBar: 🔍 Zoom | ✥ Pan | 📷 Download PNG | ↺ Reset", ha='center', va='center', fontsize=8.5, color='#475569')

# Draw curved interactive line
x_p = np.linspace(0.1, 0.9, 100)
y_p = 0.45 + 0.25 * np.sin(x_p * 7)
ax.plot(x_p, y_p, color='#0ea5e9', linewidth=3, label='Real-time Sensor Stream')
ax.fill_between(x_p, y_p, 0.2, color='#0ea5e9', alpha=0.1)

# Highlight a point with hover tooltip
hover_x, hover_y = x_p[45], y_p[45]
ax.plot(hover_x, hover_y, marker='o', markersize=10, color='#f43f5e', markeredgecolor='white', markeredgewidth=2)

# Tooltip box
rect_tt = plt.Rectangle((hover_x + 0.02, hover_y + 0.03), 0.22, 0.14, facecolor='#1e293b', edgecolor='#0ea5e9', linewidth=1.5)
ax.add_patch(rect_tt)
ax.text(hover_x + 0.13, hover_y + 0.10, "Hover Tooltip\nX: 2026-11-24\nY: $84.50\nStatus: Optimal", ha='center', va='center', fontsize=8, color='#f8fafc', linespacing=1.4)

# Range Slider at bottom
rect_rs = plt.Rectangle((0.1, 0.12), 0.8, 0.08, facecolor='#e2e8f0', edgecolor='#64748b', linewidth=1)
ax.add_patch(rect_rs)
ax.plot(x_p, 0.12 + 0.08 * (y_p - min(y_p)) / (max(y_p) - min(y_p)), color='#64748b', linewidth=1)
rect_handles = plt.Rectangle((0.25, 0.11), 0.5, 0.10, facecolor='#38bdf8', alpha=0.3, edgecolor='#0284c7', linewidth=1.5)
ax.add_patch(rect_handles)
ax.text(0.5, 0.06, "Interactive Range Slider & Timeline Selector (Click and Drag)", ha='center', va='center', fontsize=9, fontweight='bold', color='#0369a1')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.tight_layout()
plt.savefig("images/plotly_interactive_dashboard.png", dpi=200, bbox_inches='tight')
plt.close()

print("All 6 high-res sample images generated with clean fonts!")
