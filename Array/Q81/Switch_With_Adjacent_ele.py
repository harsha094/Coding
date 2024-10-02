def switch_with_adjacent_element(arr, n):
    if n <= 1:
        return arr
    for i in range(1, n, 2):
        arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr
        

n = int(input())
arr = list(map(int, input().split()))
res = switch_with_adjacent_element(arr, n)
print(*res)

'''
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3
'''