import matplotlib.pyplot as plt
import numpy as np

def spiral_matrix(n, start=1, step=1):
    # Spiralni boshlash va tartibni aniqlash
    matrix = np.zeros((n, n), dtype=int)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_idx = 0
    
    x, y = 0, 0
    current_value = start
    for _ in range(n * n):
        matrix[x, y] = current_value
        current_value += step
        
        # Keyingi katakni hisoblash
        nx, ny = x + directions[direction_idx][0], y + directions[direction_idx][1]
        
        # Agar yangi katak tashqariga chiqsa, yo'nalishni o'zgartirish
        if not (0 <= nx < n and 0 <= ny < n and matrix[nx, ny] == 0):
            direction_idx = (direction_idx + 1) % 4  # Yo'nalishni o'zgartirish
            nx, ny = x + directions[direction_idx][0], y + directions[direction_idx][1]
        
        x, y = nx, ny
    
    return matrix

# Spiral yaratish
n = 7  # Spiralning o'lchami (7x7 jadval)
spiral_asc = spiral_matrix(n)  # 1 dan n^2 gacha
spiral_desc = spiral_matrix(n, start=n*n, step=-1) # 49 dan 1 gacha

# Visualizatsiya
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 1-jadval (1 dan n^2 gacha spiral)
axes[0].imshow(spiral_asc, cmap='viridis', interpolation='none')
axes[0].set_title(f"1 dan {n**2} gacha Spiral")
axes[0].axis('off')

# Add numbers to cells for the first spiral
for i in range(n):
    for j in range(n):
        axes[0].text(j, i, str(spiral_asc[i, j]), ha='center', va='center', color='white')

# 2-jadval (n^2 dan 1 gacha spiral)
axes[1].imshow(spiral_desc, cmap='viridis', interpolation='none')
axes[1].set_title(f"{n**2} dan 1 gacha Spiral")
axes[1].axis('off')

# Add numbers to cells for the second spiral
for i in range(n):
    for j in range(n):
        axes[1].text(j, i, str(spiral_desc[i, j]), ha='center', va='center', color='white')


plt.tight_layout()
plt.show()
