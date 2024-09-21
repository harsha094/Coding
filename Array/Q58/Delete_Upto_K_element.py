N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Explicitly delete the last K elements
del arr[N-K:N]

# Print the remaining elements
print(*arr)


'''
Sample Testcase :
INPUT
5 4
1 2 3 4 5
OUTPUT
1
'''