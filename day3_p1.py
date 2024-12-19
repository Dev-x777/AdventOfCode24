import re

# Use raw string for the file path to handle backslashes
file_path = r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_03.in"

with open(file_path) as fin:
    line = fin.read().strip()

# Regex pattern to match mul(x, y) where x and y are digits
matches = re.findall(r"mul\((\d+),(\d+)\)", line)

ans = 0
# Process each match and calculate the product
for match in matches:
    ans += int(match[0]) * int(match[1])

print(ans)
