def reachTarget(arr):
    n = len(arr)
    operations = 0
    prev = 0
    
    for i in range(n):
        if arr[i] > prev:
            operations += arr[i] - prev
        prev = arr[i]
    
    return operations

# Example usage:
n = int(input())  # Read the number of elements
target_array = [int(input()) for _ in range(n)]  # Read the target array

result = reachTarget(target_array)
print(result)

'''
Sample Input

3
1
2
1
Sample Output

2
Explanation

The required task can be done in 2 operations.

First by choosing subarray [1,3] making array  = {1, 1, 1}.

Finally choosing subarray [2,2] makes array  = {1, 2, 1}, which is now, equal to the target array.

'''