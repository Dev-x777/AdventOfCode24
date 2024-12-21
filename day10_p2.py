from functools import lru_cache

with open("./day_10.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)
m = len(grid[0])  # Handle rectangular grids

# Directions for movement: up, down, left, right
dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Check if a cell is within the grid
def in_grid(i, j):
    return 0 <= i < n and 0 <= j < m

@lru_cache(None)
def rating(i, j):
    # If the current position is height 9, it's the end of a valid trail
    if grid[i][j] == "9":
        return 1

    ans = 0
    # Explore neighbors
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if in_grid(ii, jj) and int(grid[ii][jj]) == int(grid[i][j]) + 1:
            ans += rating(ii, jj)
    
    return ans

# Calculate the total rating
total_rating = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "0":  # Only consider trailheads
            total_rating += rating(i, j)

print(total_rating)
