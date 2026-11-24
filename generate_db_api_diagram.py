import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']

fig, ax = plt.subplots(figsize=(12, 6.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')

# Center: Jupyter Notebook Hub
center_box = plt.Rectangle((0.36, 0.40), 0.28, 0.22, facecolor='#f5f3ff', edgecolor='#7c3aed', linewidth=2.5, zorder=3)
ax.add_patch(center_box)
ax.text(0.50, 0.54, "Jupyter Notebook", ha='center', va='center', fontsize=14, fontweight='bold', color='#6d28d9', zorder=4)
ax.text(0.50, 0.46, "(IPython Kernel Engine)\nData Science Hub", ha='center', va='center', fontsize=10, color='#4c1d95', zorder=4)

# Top Left: File Storage (CSV, Excel, JSON)
box_files = plt.Rectangle((0.05, 0.70), 0.26, 0.22, facecolor='#e0f2fe', edgecolor='#0284c7', linewidth=1.8)
ax.add_patch(box_files)
ax.text(0.18, 0.85, "1. File Storage", ha='center', va='center', fontsize=12, fontweight='bold', color='#0369a1')
ax.text(0.18, 0.76, "• CSV (pd.read_csv)\n• Excel (.xlsx / openpyxl)\n• JSON (json.loads / pd.json_normalize)", ha='center', va='center', fontsize=9, color='#0c4a6e', linespacing=1.4)

# Bottom Left: Relational SQL Databases (PostgreSQL, SQLite)
box_sql = plt.Rectangle((0.05, 0.10), 0.26, 0.22, facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8)
ax.add_patch(box_sql)
ax.text(0.18, 0.25, "2. Relational SQL", ha='center', va='center', fontsize=12, fontweight='bold', color='#065f46')
ax.text(0.18, 0.16, "• SQLite (sqlite3 / In-Memory)\n• PostgreSQL (psycopg2 / SQLAlchemy)\n• %sql IPython Magics", ha='center', va='center', fontsize=9, color='#064e3b', linespacing=1.4)

# Top Right: Web & Cloud APIs (REST APIs, Requests)
box_api = plt.Rectangle((0.69, 0.70), 0.26, 0.22, facecolor='#fef3c7', edgecolor='#d97706', linewidth=1.8)
ax.add_patch(box_api)
ax.text(0.82, 0.85, "3. Cloud REST APIs", ha='center', va='center', fontsize=12, fontweight='bold', color='#92400e')
ax.text(0.82, 0.76, "• requests (GET, POST, PUT, DEL)\n• Authentication (Bearer / JWT)\n• JSON Response to DataFrame", ha='center', va='center', fontsize=9, color='#78350f', linespacing=1.4)

# Bottom Right: Real-time & In-Memory (Redis, WebSockets)
box_rt = plt.Rectangle((0.69, 0.10), 0.26, 0.22, facecolor='#ffe4e6', edgecolor='#e11d48', linewidth=1.8)
ax.add_patch(box_rt)
ax.text(0.82, 0.25, "4. Fast Cache & Streaming", ha='center', va='center', fontsize=12, fontweight='bold', color='#9f1239')
ax.text(0.82, 0.16, "• Redis (In-Memory Key/Value, Hash)\n• WebSockets (Live Data Feeds)\n• Stock Tickers & IoT Telemetry", ha='center', va='center', fontsize=9, color='#881337', linespacing=1.4)

# Connecting Arrows
ax.annotate("", xy=(0.36, 0.55), xytext=(0.28, 0.70), arrowprops=dict(arrowstyle="<->", color='#0284c7', lw=2))
ax.annotate("", xy=(0.36, 0.45), xytext=(0.28, 0.30), arrowprops=dict(arrowstyle="<->", color='#059669', lw=2))
ax.annotate("", xy=(0.64, 0.55), xytext=(0.72, 0.70), arrowprops=dict(arrowstyle="<->", color='#d97706', lw=2))
ax.annotate("", xy=(0.64, 0.45), xytext=(0.72, 0.30), arrowprops=dict(arrowstyle="<->", color='#e11d48', lw=2))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.suptitle("Jupyter Notebook: Enterprise Database & API Integration Ecosystem", fontsize=15, fontweight='bold', color='#0f172a', y=0.98)
plt.tight_layout()
plt.savefig("images/database_api_architecture.png", dpi=200, bbox_inches='tight')
plt.close()
print("Database & API Architecture diagram generated successfully!")
