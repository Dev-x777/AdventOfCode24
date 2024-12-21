from collections import defaultdict
from itertools import combinations

# Read the input grid
with open("C:\\Users\\devje\\OneDrive\\Desktop\\adventOfCode\\day_08.in") as fin:
    grid = [line.strip() for line in fin.read().strip().split("\n")]

# Determine grid dimensions
n = len(grid)
m = max(len(row) for row in grid)  # Handle rows of varying lengths

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < m

def get_antinodes(a, b):
    ax, ay = a
    bx, by = b
    
    cx, cy = ax - (bx - ax), ay - (by - ay)
    dx, dy = bx + (bx - ax), by + (by - ay)

    if in_bounds(cx, cy):
        yield (cx, cy)
    if in_bounds(dx, dy):
        yield (dx, dy)

# Collect antinodes
antinodes = set()

# Group locations by frequency (symbol)
all_locs = defaultdict(list)
for i in range(n):
    for j in range(len(grid[i])):  # Use the actual row length
        if grid[i][j] != ".":
            all_locs[grid[i][j]].append((i, j))

# Process combinations to find antinodes
for freq in all_locs:
    locs = all_locs[freq]
    for a, b in combinations(locs, r=2):
        for antinode in get_antinodes(a, b):
            antinodes.add(antinode)

# Output the number of unique antinodes
print(len(antinodes))
