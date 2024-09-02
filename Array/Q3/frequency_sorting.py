n = int(input())
arr = list(map(int, input().split()))
# Count frequency of each element in the array
from collections import Counter
frequency = Counter(arr)
# Sort the array: first by frequency, then by value
sorted_arr = sorted(set(arr), key=lambda x: (frequency[x],x))

# Print the sorted array
print(" ".join(map(str, sorted_arr)))
# Sample Input :
# 4
# 1 1 3 2
# Sample Output :
# 2 3 1