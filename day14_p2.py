with open("./day_14.in") as fin:
    lines = fin.read().strip().split("\n")

# Grid dimensions
n = 103
m = 101

# Positions and velocities of robots
p = []
v = []

# Parsing input
for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(list(map(int, b.split("=")[1].split(","))))

    # Swap x and y coordinates for consistency with the grid
    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

N = len(p)  # Number of robots

# Update function to move robots
def update_positions():
    for i in range(N):
        p[i][0] = (p[i][0] + v[i][0] + n) % n
        p[i][1] = (p[i][1] + v[i][1] + m) % m

# Function to count robots in a subgrid
def count_robots_in_subgrid(i0, i1, j0, j1):
    return sum(1 for x, y in p if i0 <= x < i1 and j0 <= y < j1)

# Function to check for Christmas tree pattern
def check_christmas_tree():
    grid = [["." for _ in range(m)] for _ in range(n)]
    for x, y in p:
        grid[x][y] = "#"

    # Example Christmas tree pattern
    christmas_tree = [
        ".....#.....",
        "....###....",
        "...#####...",
        "..#######..",
        ".#########.",
        "....###....",
        "....###...."
    ]

    tree_height = len(christmas_tree)
    tree_width = len(christmas_tree[0])

    for i in range(n - tree_height + 1):
        for j in range(m - tree_width + 1):
            match = True
            for di in range(tree_height):
                for dj in range(tree_width):
                    if (
                        christmas_tree[di][dj] == "#"
                        and grid[i + di][j + dj] != "#"
                    ):
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

# Simulate until the Easter egg appears
time = 0
while True:
    if check_christmas_tree():
        break
    update_positions()
    time += 1

print(f"The Christmas tree appears after {time} seconds.")
