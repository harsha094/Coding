N,M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr = arr1 + arr2
arr.sort()
print(*arr)

'''
Sample Testcase :
INPUT
5 4
1 2 3 4 5
1 2 3 4
OUTPUT
1 1 2 2 3 3 4 4 5
'''