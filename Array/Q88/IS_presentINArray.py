def binary_search(arr, N, K):
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return "yes"
        elif arr[mid] < K:
            low = mid + 1
        else:
            high = mid - 1
    return 'no'

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Search for the element K
print(binary_search(arr, N, K))
'''
Sample Testcase :
INPUT
3 2
2 3 7
OUTPUT
Yes

'''