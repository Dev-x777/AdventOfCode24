# Define the function to calculate the next secret number in the sequence
def next_secret_number(secret):
    for _ in range(2000):
        # Step 1: Multiply by 64, mix, and prune
        secret = (secret ^ (secret * 64)) % 16777216
        # Step 2: Divide by 32, round down, mix, and prune
        secret = (secret ^ (secret // 32)) % 16777216
        # Step 3: Multiply by 2048, mix, and prune
        secret = (secret ^ (secret * 2048)) % 16777216
    return secret

# Read input from a file
with open(r"C:\Users\devje\OneDrive\Desktop\adventOfCode\day_22.in", "r") as file:
    initial_secrets = [int(line.strip()) for line in file]

# Calculate the 2000th secret number for each buyer and sum them up
result_sum = sum(next_secret_number(secret) for secret in initial_secrets)

# Output the result
print("The sum of the 2000th secret number for each buyer is:", result_sum)
