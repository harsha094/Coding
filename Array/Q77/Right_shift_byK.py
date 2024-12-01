def right_shift_k_times(arr, K, N):
    # Normalize K to avoid unnecessary rotations
    K = K % N
    # Split and concatenate
    if K == 0:
        return arr
    else:
        return arr[-K:] + arr[:-K]
#Inputs    
N,K = map(int, input().split())
arr = list(map(int, input().split()))
res = right_shift_k_times(arr, K, N)
# Print Output
print(*res)

'''
Sample Testcase :
INPUT
3 2
7 2 3
OUTPUT
2 3 7

'''
