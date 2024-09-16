n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(" ".join(map(str, arr)))

'''

Sample Input :
8
7000 8000 6500 1200 4000 2800 3000 5230
Sample Output :
1200 2800 3000 4000 5230 6500 7000 8000

'''