import matplotlib.pyplot as plt
import numpy as np

def spiral_matrix(n):
  
    matrix = np.zeros((n, n), dtype=int)
 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0  
    
    x, y = 0, 0  
    num = 1 
    
    for _ in range(n * n):
        matrix[x][y] = num  
        num += 1
       
        next_x = x + directions[direction_idx][0]
        next_y = y + directions[direction_idx][1]
        
  
        if (
            next_x < 0 or next_x >= n or  
            next_y < 0 or next_y >= n or
            matrix[next_x][next_y] != 0  
        ):
            direction_idx = (direction_idx + 1) % 4  
            next_x = x + directions[direction_idx][0]
            next_y = y + directions[direction_idx][1]
        
        x, y = next_x, next_y  
    
    return matrix

n = 7
spiral = spiral_matrix(n)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(spiral, cmap='viridis', interpolation='none')

for i in range(n):
    for j in range(n):
        ax.text(j, i, str(spiral[i, j]),
                ha='center', va='center', color='white', fontsize=12)

ax.axis('off')

plt.title("Spiral Matritsa (7x7) 1 dan 49 gacha", fontsize=16, pad=20)
plt.show()
