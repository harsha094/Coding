def find_kth_smallest(arr, n, k):
    # Check if K is valid
    if k < 1 or k > n:
        return -1
    
    # Sort the array
    arr.sort()
    
    unique_count = 0
    prev = float('-inf')  # Use negative infinity as initial value
    
    # Iterate through the sorted array
    for num in arr:
        if num != prev:
            unique_count += 1
            if unique_count == k:
                return num
        prev = num
    
    # If K unique elements are not found
    return -1

# Input handling

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = find_kth_smallest(arr, n, k)
print(result)


'''
Sample Testcase :
INPUT
5 2
1 1 2 4 5
OUTPUT
2
'''