ans = 0
a = []
b = []

# Use raw string for file path to handle backslashes
file_path = r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_01.in"

with open(file_path) as fin:
    data = fin.read()

for line in data.strip().split("\n"):
    if line.strip():  # Ignore empty lines
        try:
            nums = [int(i) for i in line.split() if i.strip()]  # Split and validate
            if len(nums) == 2:  # Ensure exactly two numbers are present
                a.append(nums[0])
                b.append(nums[1])
            else:
                print(f"Skipping invalid line (not exactly two numbers): {line}")
        except ValueError:
            print(f"Skipping non-numeric line: {line}")

# Ensure both lists have the same length before sorting and calculating the result
if len(a) == len(b):
    a.sort()
    b.sort()

    for i in range(len(a)):
        ans += abs(a[i] - b[i])

    print(f"Final answer: {ans}")
else:
    print("Error: Lists 'a' and 'b' have unequal lengths.")
