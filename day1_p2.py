from collections import defaultdict

# Use raw string for file path to handle backslashes
file_path = r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_01.in"

with open(file_path) as fin:
    data = fin.read()

ans = 0
a = []
b = []

# Split each line correctly
for line in data.strip().split("\n"):
    if line.strip():  # Ensure the line is not empty
        try:
            nums = [int(i) for i in line.split()]  # Split by any whitespace
            if len(nums) == 2:  # Ensure there are exactly two numbers
                a.append(nums[0])
                b.append(nums[1])
            else:
                print(f"Skipping invalid line (not exactly two numbers): {line}")
        except ValueError:
            print(f"Skipping non-numeric line: {line}")

# Use defaultdict to count occurrences of elements in b
counts = defaultdict(int)
for x in b:
    counts[x] += 1

# Calculate the answer by multiplying elements in a by the frequency of corresponding elements in b
for x in a:
    ans += x * counts[x]

print(f"Final answer: {ans}")
