def find_longest_repeating_sequence(arr, n):
    if n == 0:
        print(-1)
        return
        
    longest_seq = 1
    current_seq = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            current_seq += 1
            longest_seq = max(longest_seq, current_seq)
        else:
            current_seq = 1

    # If no repeating sequence is found, return -1
    if longest_seq == 1:
        print(-1)
    else:
        print(longest_seq)
        
# Input handling
n = int(input())
arr = list(map(int, input().split()))
find_longest_repeating_sequence(arr, n)

# Sample Testcase :
# INPUT
# 8
# 1 2 2 2 3 4 5 6
# OUTPUT
# 3