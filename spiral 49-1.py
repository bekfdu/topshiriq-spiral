import matplotlib.pyplot as plt
import numpy as np

def reverse_spiral_matrix(n):
    # Create an empty matrix
    matrix = np.zeros((n, n), dtype=int)
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0  # Start with the right direction

    x, y = 0, 0  # Starting position
    num = n * n  # Start with the largest number

    for _ in range(n * n):
        matrix[x][y] = num  # Fill the current position
        num -= 1

        # Calculate the next position
        next_x = x + directions[direction_idx][0]
        next_y = y + directions[direction_idx][1]

        # Check if we need to change direction
        if (
            next_x < 0 or next_x >= n or  # Out of bounds
            next_y < 0 or next_y >= n or
            matrix[next_x][next_y] != 0  # Already filled
        ):
            direction_idx = (direction_idx + 1) % 4  # Change direction
            next_x = x + directions[direction_idx][0]
            next_y = y + directions[direction_idx][1]

        x, y = next_x, next_y  # Move to the next position

    return matrix

# Generate the 7x7 reverse spiral matrix
n = 7
reverse_spiral = reverse_spiral_matrix(n)

# Plot the matrix using matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(reverse_spiral, cmap='viridis', interpolation='none')

# Annotate each cell with the corresponding number
for i in range(n):
    for j in range(n):
        ax.text(j, i, str(reverse_spiral[i, j]),
                ha='center', va='center', color='white', fontsize=12)

# Remove axes for a cleaner look
ax.axis('off')

# Display the plot
plt.title("Spiral Matritsa (7x7) 49 dan 1 gacha", fontsize=16, pad=20)
plt.show()
