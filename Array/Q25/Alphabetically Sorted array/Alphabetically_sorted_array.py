n = int(input())
arr = list(map(str, input().split()))
arr.sort()
print(" ".join(map(str, arr)))

'''
Sample Input :
3
InfinityWar EndGame Avengers
Sample Output :
Avengers EndGame InfinityWar

'''