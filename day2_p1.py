ans = 0

# Use raw string `r""` or escape the backslashes for the file path
file_path = r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_02.in"

with open(file_path) as fin:
    lines = fin.read().strip().split("\n")

def is_safe(nums):
    """
    Determines if a sequence of numbers is safe.
    A sequence is safe if:
    - For increasing sequences: Differences between consecutive numbers are in the range [1, 3].
    - For decreasing sequences: Differences between consecutive numbers are in the range [-3, -1].
    """
    if len(nums) < 2:
        return False  # A safe sequence requires at least two numbers
    inc = nums[1] > nums[0]  # Determine if the sequence is increasing
    if inc:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if not -3 <= diff <= -1:
                return False
        return True

for line in lines:
    if line.strip():  # Ensure the line is not empty
        try:
            nums = [int(i) for i in line.split()]  # Convert each number in the line
            print(f"Processing sequence: {nums}")  # Debugging: print the current sequence
            result = is_safe(nums)
            print(f"Is safe: {result}")  # Debugging: show if the sequence is safe
            ans += result  # Increment by 1 if the sequence is safe
        except ValueError:
            print(f"Skipping invalid line: {line}")  # Debugging: handle non-numeric data

print(f"Final answer: {ans}")
