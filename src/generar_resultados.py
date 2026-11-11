"""Regenera las gráficas y siete etapas desde los puntos CSV."""
from pathlib import Path
import csv, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from spline import construir, evaluar

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / 'assets' / 'puerta_del_sol_visualizacion.png'
CSV = ROOT / 'data' / 'puntos_control.csv'
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
img = Image.open(IMG).convert('RGB')
with CSV.open(encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
pts = np.array([[float(r['x_px']), float(r['y_px'])] for r in rows])
t, cx, cy = construir(pts)
s = np.linspace(t[0], t[-1], 1400)
curve = np.column_stack([evaluar(t, cx, s), evaluar(t, cy, s)])
plt.rcParams['font.family'] = 'DejaVu Sans'

def base(ax):
    ax.imshow(img)
    ax.set_xlim(0, img.width)
    ax.set_ylim(img.height, 0)
    ax.axis('off')

fig, ax = plt.subplots(figsize=(13, 8)); base(ax)
ax.plot(pts[:, 0], pts[:, 1], '-o', color='#ffd36e', lw=2.5, ms=7)
for i, (x, y) in enumerate(pts, 1):
    ax.annotate(f'P{i}', (x, y), xytext=(6, -13), textcoords='offset points', color='white', fontsize=8)
fig.savefig(OUT/'01_puntos_control.png', dpi=140, bbox_inches='tight', pad_inches=0); plt.close(fig)

fig, ax = plt.subplots(figsize=(13, 8)); base(ax)
ax.plot(curve[:, 0], curve[:, 1], color='#64f0a8', lw=5)
ax.scatter(pts[:, 0], pts[:, 1], c='#ffd36e', s=35, edgecolors='#1a2026', zorder=4)
fig.savefig(OUT/'02_spline_superpuesto.png', dpi=140, bbox_inches='tight', pad_inches=0); plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 9))
ax.plot(curve[:, 0], curve[:, 1], color='#8b5a2b', lw=4)
ax.scatter(pts[:, 0], pts[:, 1], c='#d79a44', s=38, zorder=3)
ax.set_xlim(560, 1000); ax.set_ylim(1010, 380); ax.set_aspect('equal')
ax.grid(alpha=.22); ax.set_title('Reconstrucción matemática del vano central')
ax.set_xlabel('Coordenada X (px)'); ax.set_ylabel('Coordenada Y (px)')
fig.savefig(OUT/'03_reconstruccion.png', dpi=150, bbox_inches='tight'); plt.close(fig)

labels = ['Pieza seleccionada', 'Zona de reconstrucción', 'Puntos de control', 'Primeros segmentos', 'Spline completo', 'Reconstrucción digital', 'Resultado final']
for k in range(1, 8):
    fig, ax = plt.subplots(figsize=(13, 8)); base(ax)
    n = min(len(pts), round(k / 7 * len(pts)))
    if n: ax.scatter(pts[:n, 0], pts[:n, 1], s=45, c='#ffd36e', edgecolors='#1a2026', zorder=4)
    if k >= 4:
        frac = (k - 3) / 4
        ax.plot(curve[:max(2, int(frac * len(curve))), 0], curve[:max(2, int(frac * len(curve))), 1], color='#64f0a8', lw=4)
    if k >= 6: ax.plot(curve[:, 0], curve[:, 1], color='#64f0a8', lw=5)
    ax.set_title(f'ETAPA {k} DE 7 · {labels[k-1]}', color='#f5e6c8')
    fig.savefig(OUT / f'paso_{k}.png', dpi=120, bbox_inches='tight', facecolor='#17232a'); plt.close(fig)
print('Gráficas y siete etapas regeneradas en', OUT)
