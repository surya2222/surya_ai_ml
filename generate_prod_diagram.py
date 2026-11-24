import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']

fig, ax = plt.subplots(figsize=(13, 7.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')

# Production Jupyter 4-Tier Architecture
tiers = [
    {
        "title": "1. Environment & Setup",
        "desc": "• Virtual Envs (venv / conda)\n• Package Management (pip)\n• requirements.txt / env.yml\n• ipykernel Environment Linking",
        "color": "#f0fdf4", "edge": "#16a34a", "x": 0.04, "y": 0.55
    },
    {
        "title": "2. Quality & Versioning",
        "desc": "• Git Version Control\n• nbstripout / nbdime Visual Diffs\n• Automated Testing (nbval / pytest)\n• Defensive Code Assertions",
        "color": "#e0f2fe", "edge": "#0284c7", "x": 0.28, "y": 0.55
    },
    {
        "title": "3. Automation & Lab",
        "desc": "• JupyterLab Workspace & Docks\n• Papermill Parameterized Execution\n• Scheduled Cron / Airflow Pipelines\n• Headless Automated Reporting",
        "color": "#faf5ff", "edge": "#9333ea", "x": 0.52, "y": 0.55
    },
    {
        "title": "4. Enterprise Deployment",
        "desc": "• Remote Access (SSH Tunneling)\n• Cloud Notebooks (Colab / Kaggle)\n• Security (Argon2 Passwords, SSL)\n• nbconvert (No-Code HTML / PDF)",
        "color": "#fff1f2", "edge": "#e11d48", "x": 0.76, "y": 0.55
    }
]

for t in tiers:
    box = plt.Rectangle((t['x'], t['y']), 0.20, 0.33, facecolor=t['color'], edgecolor=t['edge'], linewidth=2, zorder=2)
    ax.add_patch(box)
    ax.text(t['x'] + 0.10, t['y'] + 0.28, t['title'], ha='center', va='center', fontsize=11, fontweight='bold', color=t['edge'])
    ax.text(t['x'] + 0.02, t['y'] + 0.13, t['desc'], ha='left', va='center', fontsize=8.5, color='#1e293b', linespacing=1.5)

# Connecting Pipeline Arrows
ax.annotate("", xy=(0.28, 0.71), xytext=(0.24, 0.71), arrowprops=dict(arrowstyle="->", color='#16a34a', lw=2.5))
ax.annotate("", xy=(0.52, 0.71), xytext=(0.48, 0.71), arrowprops=dict(arrowstyle="->", color='#0284c7', lw=2.5))
ax.annotate("", xy=(0.76, 0.71), xytext=(0.72, 0.71), arrowprops=dict(arrowstyle="->", color='#9333ea', lw=2.5))

# Bottom Banner: Production Standards & Golden Rules
box_banner = plt.Rectangle((0.04, 0.10), 0.92, 0.32, facecolor='#f8fafc', edgecolor='#64748b', linewidth=1.8, linestyle='--', zorder=2)
ax.add_patch(box_banner)
ax.text(0.50, 0.35, "★ The 5 Pillars of Production-Grade Jupyter Notebooks ★", ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

rules_text = (
    "1. Reproducibility: Clean 'Restart & Run All' execution with fixed random seeds (random_state=42).\n"
    "2. Modularity: Refactor heavy logic into standalone .py modules; keep notebooks clean, narrative and focused.\n"
    "3. Security: Never hardcode passwords or API keys; use .env and restrict remote server access via SSH tunnels.\n"
    "4. Clean Version Control: Use nbstripout to prevent bloated git commit diffs from binary chart outputs.\n"
    "5. Automated Execution: Leverage Papermill to schedule batch jobs and publish automated stakeholder reports."
)
ax.text(0.08, 0.21, rules_text, ha='left', va='center', fontsize=9, color='#334155', linespacing=1.6)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.suptitle("Production-Level Jupyter: Enterprise Architecture, Automation & Governance", fontsize=15, fontweight='bold', color='#0f172a', y=0.98)
plt.tight_layout()
plt.savefig("images/production_jupyter_architecture.png", dpi=200, bbox_inches='tight')
plt.close()
print("Production Jupyter Architecture diagram generated successfully!")
