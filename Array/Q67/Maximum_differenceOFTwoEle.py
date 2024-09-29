def max_difference(arr):
    # If array length is less than 2, no valid difference can be found
    if len(arr) < 2:
        return 0

    # Initialize min_element with the first element and max_diff to negative infinity
    min_element = arr[0]
    max_diff = arr[1] - arr[0]

    # Traverse the array starting from the second element
    for i in range(1, len(arr)):
        # Update max_diff if the current difference is greater
        max_diff = max(max_diff, arr[i] - min_element)

        # Update min_element to the minimum element found so far
        min_element = min(min_element, arr[i])

    return max_diff

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Find and print the maximum difference
print(max_difference(arr))


'''
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
4
'''