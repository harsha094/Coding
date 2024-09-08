n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    if arr[i] < 0:
        sum += arr[i]
print(sum)

'''
Sample Testcase :
INPUT
2
3 0
OUTPUT
0
'''