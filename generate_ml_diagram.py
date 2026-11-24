import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']

fig, ax = plt.subplots(figsize=(13, 7.5))
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#ffffff')

# Stages of End-to-End Data Science & Machine Learning Pipeline
stages = [
    {"title": "1. Data Cleaning & Prep", "desc": "• Missing Imputation\n• Outlier Capping (IQR)\n• Deduplication\n• Scaling & Encoding", "color": "#e0f2fe", "edge": "#0284c7", "x": 0.04, "y": 0.55},
    {"title": "2. EDA & Statistics", "desc": "• Univariate & Bivariate\n• Correlation Matrix\n• Distributions (Normal, CLT)\n• Feature Selection", "color": "#fef3c7", "edge": "#d97706", "x": 0.28, "y": 0.55},
    {"title": "3. Machine Learning", "desc": "• Regression (Linear, Ridge)\n• Classification (Trees, RF)\n• Clustering (K-Means, Hierarchical)\n• Cross-Validation", "color": "#f3e8ff", "edge": "#7c3aed", "x": 0.52, "y": 0.55},
    {"title": "4. Evaluation & Saving", "desc": "• Confusion Matrix\n• Precision, Recall, F1\n• ROC-AUC & RMSE\n• Model Saving (Joblib)", "color": "#ecfdf5", "edge": "#059669", "x": 0.76, "y": 0.55},
]

for s in stages:
    box = plt.Rectangle((s['x'], s['y']), 0.20, 0.32, facecolor=s['color'], edgecolor=s['edge'], linewidth=2, zorder=2)
    ax.add_patch(box)
    ax.text(s['x'] + 0.10, s['y'] + 0.27, s['title'], ha='center', va='center', fontsize=11, fontweight='bold', color=s['edge'])
    ax.text(s['x'] + 0.02, s['y'] + 0.13, s['desc'], ha='left', va='center', fontsize=8.5, color='#1e293b', linespacing=1.5)

# Connecting Arrows
ax.annotate("", xy=(0.28, 0.71), xytext=(0.24, 0.71), arrowprops=dict(arrowstyle="->", color='#0284c7', lw=2.5))
ax.annotate("", xy=(0.52, 0.71), xytext=(0.48, 0.71), arrowprops=dict(arrowstyle="->", color='#d97706', lw=2.5))
ax.annotate("", xy=(0.76, 0.71), xytext=(0.72, 0.71), arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=2.5))

# Bottom Tier: Advanced Modern Horizons (Deep Learning & GenAI LLM Integration)
box_dl = plt.Rectangle((0.15, 0.10), 0.32, 0.28, facecolor='#fff1f2', edgecolor='#e11d48', linewidth=2, zorder=2)
ax.add_patch(box_dl)
ax.text(0.31, 0.33, "5. Deep Learning (DL)", ha='center', va='center', fontsize=11, fontweight='bold', color='#be123c')
ax.text(0.18, 0.21, "• Neural Networks (ANN, CNN, RNN)\n• TensorFlow / Keras Sequential API\n• PyTorch Tensors, Autograd & nn.Module\n• GPU Acceleration (CUDA)", ha='left', va='center', fontsize=8.5, color='#881337', linespacing=1.5)

box_ai = plt.Rectangle((0.53, 0.10), 0.32, 0.28, facecolor='#eff6ff', edgecolor='#2563eb', linewidth=2, zorder=2)
ax.add_patch(box_ai)
ax.text(0.69, 0.33, "6. Modern AI & GenAI", ha='center', va='center', fontsize=11, fontweight='bold', color='#1d4ed8')
ax.text(0.56, 0.21, "• LLM APIs (Gemini, Claude, GPT)\n• Dense Vector Embeddings\n• Cosine Similarity & Vector Search\n• RAG (Retrieval-Augmented Generation)", ha='left', va='center', fontsize=8.5, color='#1e3a8a', linespacing=1.5)

# Downward arrows from ML to DL and AI
ax.annotate("", xy=(0.31, 0.38), xytext=(0.40, 0.55), arrowprops=dict(arrowstyle="->", color='#e11d48', lw=2, linestyle='--'))
ax.annotate("", xy=(0.69, 0.38), xytext=(0.62, 0.55), arrowprops=dict(arrowstyle="->", color='#2563eb', lw=2, linestyle='--'))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.suptitle("End-to-End Data Science, Machine Learning, Deep Learning & AI Ecosystem", fontsize=15, fontweight='bold', color='#0f172a', y=0.98)
plt.tight_layout()
plt.savefig("images/ml_pipeline_architecture.png", dpi=200, bbox_inches='tight')
plt.close()
print("ML Pipeline Architecture diagram generated successfully!")
