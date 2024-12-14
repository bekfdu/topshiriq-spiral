import matplotlib.pyplot as plt
import numpy as np

def spiral_matrix(n, start=1, step=1):
    # Spiralni boshlash va tartibni aniqlash
    matrix = np.zeros((n, n), dtype=int)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_idx = 0
    
    x, y = 0, 0
…# Add numbers to cells for the second spiral
for i in range(n):
    for j in range(n):
        axes[1].text(j, i, str(spiral_desc[i, j]), ha='center', va='center', color='white')


plt.tight_layout()
plt.show()
