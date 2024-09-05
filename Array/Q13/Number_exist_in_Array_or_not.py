n, k = map(int, input().split())
arr = list(map(int, input().split()))
s = set(arr)
if k in s:
    print("yes")
else:
    print("no")

'''
Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes

'''