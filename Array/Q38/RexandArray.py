import math
from itertools import combinations
from collections import Counter

def gcd_sum_of_frequencies(n, chars):
    # Frequency array for digits 0-9
    freq = [0] * 10
    
    # Count the frequency of each digit
    for char in chars:
        digit = int(char)
        freq[digit] += 1
    
    # Extract non-zero frequencies
    non_zero_freq = [f for f in freq if f > 0]
    
    # Special case: If there's only one distinct element
    if len(non_zero_freq) == 1:
        return non_zero_freq[0]
    
    # Calculate sum of GCDs of all pairs
    total_gcd_sum = 0
    for a, b in combinations(non_zero_freq, 2):
        total_gcd_sum += math.gcd(a, b)
    
    return total_gcd_sum

# Input reading
n = int(input().strip())
chars = [input().strip() for _ in range(n)]

# Compute and print result
print(gcd_sum_of_frequencies(n, chars))


'''
Sample Input

5
5
4
8
5
0
Sample Output

6
Explanation

Frequency array: freq[]={2,1,1,1}.

Possible pairs={(2,1),(2,1),(2,1),(1,1),(1,1),(1,1)}

GCD array of pairs={1,1,1,1,1,1}

Sum=6

'''