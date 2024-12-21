from collections import defaultdict
from tqdm import tqdm

# Reading the grid from input file
with open("./day_20.in") as fin:
    grid = [list(line.strip()) for line in fin.readlines()]

# Print the grid for debugging purposes
for row in grid:
    print("".join(row))  # This will show the grid in its original form.

N = len(grid)
def in_grid(i, j):
    return 0 <= i < N and 0 <= j < N

# Find the start (S) and end (E) positions
si = sj = ei = ej = None
for i in range(N):
    for j in range(N):
        if grid[i][j] == "S":
            si, sj = i, j
        elif grid[i][j] == "E":
            ei, ej = i, j

# Debugging: Check if S and E are found
print(f"Start position: {si, sj}")
print(f"End position: {ei, ej}")

# If S or E is not found, raise an error
if si is None or sj is None or ei is None or ej is None:
    raise ValueError("Start (S) or End (E) position not found in the grid.")

# Directions for moving (down, right, up, left)
dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# Determine the original path from S to E
path = [(si, sj)]
while path[-1] != (ei, ej):
    i, j = path[-1]
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if not in_grid(ii, jj):
            continue
        if len(path) > 1 and (ii, jj) == path[-2]:
            continue
        if grid[ii][jj] == "#":
            continue
        
        path.append((ii, jj))
        break

og = len(path) - 1

# Create a dictionary to store times for each coordinate
times = {}
for t, coord in enumerate(path):
    times[coord] = og - t

# Initialize counts and saved dictionary
counts = defaultdict(int)
saved = {}

# Process paths and save potential times
for t, coord in enumerate(tqdm(path, ncols=80)):
    i, j = coord
    for di1, dj1 in dd:
        for di2, dj2 in dd:
            ii, jj = i + di1 + di2, j + dj1 + dj2
            if not in_grid(ii, jj) or grid[ii][jj] == "#":
                continue

            rem_t = times.get((ii, jj), 0)
            saved[(i, j, ii, jj)] = og - (t + rem_t + 2)

# Calculate the final answer
ans = 0
for v in saved.values():
    if v >= 0: counts[v] += 1
    if v >= 100: ans += 1

print(ans)
