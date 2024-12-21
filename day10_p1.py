with open("./day_10.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)
m = len(grid[0])  # Handle rectangular grids

# Directions for movement: up, down, left, right
dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Check if a cell is within the grid
def in_grid(i, j):
    return 0 <= i < n and 0 <= j < m

# Calculate the score for a trailhead
def score(i, j):
    if grid[i][j] != "0":
        return 0

    ans = 0
    stack = [(i, j)]
    visited = set()
    visited.add((i, j))

    while stack:
        curi, curj = stack.pop()
        cur = int(grid[curi][curj])

        # If we've reached a height of 9, count it as a valid endpoint
        if cur == 9:
            ans += 1
            continue

        # Explore neighbors
        for di, dj in dd:
            ii, jj = curi + di, curj + dj

            if in_grid(ii, jj) and (ii, jj) not in visited:
                nbr = int(grid[ii][jj])
                if nbr == cur + 1:  # Ensure the path increases by exactly 1
                    stack.append((ii, jj))
                    visited.add((ii, jj))

    return ans

# Calculate the total score
total_score = 0
for i in range(n):
    for j in range(m):
        total_score += score(i, j)

print(total_score)
