ans = 0

# Use raw string or escape backslashes in the file path
file_path = r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_02.in"

with open(file_path) as fin:
    lines = fin.read().strip().split("\n")

def is_safe(nums):
    """
    Checks if the sequence of numbers is safe based on the differences between them.
    """
    if len(nums) < 2:
        return False
    inc = nums[1] > nums[0]
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
    
def is_really_safe(nums):
    """
    Checks if the sequence is safe or can be made safe by removing one element.
    """
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        # Check if removing one element makes the sequence safe
        # Ensure we are not left with an empty list after removal
        if len(nums) > 1 and is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

for line in lines:
    if line.strip():  # Ensure line is not empty
        try:
            nums = [int(i) for i in line.split()]  # Convert to integers
            ans += is_really_safe(nums)  # Add 1 if the sequence is safe
        except ValueError:
            print(f"Skipping invalid line: {line}")  # Handle invalid lines

print(f"Final answer: {ans}")
