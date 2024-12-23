import sys
import re
from collections import defaultdict

def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216

def prices(x):
    """Generate the prices for a buyer starting with secret number x."""
    ans = [x]
    for _ in range(2000):
        x = prune(mix(x, 64 * x))
        x = prune(mix(x, x // 32))
        x = prune(mix(x, x * 2048))
        ans.append(x)
    return ans

def changes(P):
    """Calculate changes between consecutive prices."""
    return [P[i + 1] - P[i] for i in range(len(P) - 1)]

def getScores(P, C):
    """Get the score for each pattern of 4 changes."""
    ANS = {}
    for i in range(len(C) - 3):
        pattern = (C[i], C[i + 1], C[i + 2], C[i + 3])
        if pattern not in ANS:
            ANS[pattern] = P[i + 4]
    return ANS

# Main execution
infile = sys.argv[1] if len(sys.argv) >= 2 else 'day_22.in'
D = open(infile).read().strip()

p1 = 0  # To store the sum of the last price of all buyers
SCORE = defaultdict(int)  # To store cumulative scores for each pattern

for line in D.split('\n'):
    P = prices(int(line))  # Generate prices
    p1 += P[-1]  # Add the last price of this buyer
    P = [x % 10 for x in P]  # Convert prices to banana count (ones digit)
    C = changes(P)  # Get the price changes
    S = getScores(P, C)  # Get scores for each pattern of changes
    for k, v in S.items():
        SCORE[k] += v  # Accumulate scores for each pattern

# Calculate results
max_score = max(SCORE.values())
best_pattern = max(SCORE, key=SCORE.get)

print(p1)  # Print the sum of the last prices of all buyers
print(max_score)  # Print the maximum score
print(best_pattern)  # Print the best pattern
