def position_of_k(arr, N, K):
    count = 0
    for i in range(N):
        count += 1
        if arr[i] == K:
            return count

N,K = map(int, input().split())
arr = list(map(int, input().split()))
res = position_of_k(arr, N, K)
if res:
    print(res)
else:
    print('-1')

'''
Sample Testcase :
INPUT
5 1
3 2 1 2 3
OUTPUT
3

'''