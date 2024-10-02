def remove_duplicate(arr):
    return list(set(arr))

n = int(input())
arr = list(map(int, input().split()))
result = remove_duplicate(arr)
print(*result)

'''
Sample Testcase :
INPUT
4
2 4 4 2
OUTPUT
2 4
'''