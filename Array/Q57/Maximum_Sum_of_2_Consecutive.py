def maximum_of_two_consecutive(arr, n):
    result = []
    for i in range(n - 1):
        current_max = max(arr[i], arr[i+1])
        result.append(current_max)
    
    print(" ".join(map(str, result)))

n = int(input())
arr = list(map(int, input().split()))

maximum_of_two_consecutive(arr, n)
'''
Sample Testcase :
INPUT
5
1 1 3 0 5
OUTPUT
1 3 3 5
'''