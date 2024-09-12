def min_swaps_to_sort(arr):
    n = len(arr)
    # Create an array of tuples where each tuple is (height, original index)
    indexed_arr = [(arr[i], i) for i in range(n)]
    
    # Sort the array by the height (first element of the tuple)
    indexed_arr.sort(key=lambda x: x[0])

    # To keep track of visited elements
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # If the element is already visited or it is already in the correct position
        if visited[i] or indexed_arr[i][1] == i:
            continue
        
        # Find cycle
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            # Move to the next index in the cycle
            j = indexed_arr[j][1]
            cycle_size += 1

        # If there is a cycle of size k, we need k-1 swaps
        if cycle_size > 1:
            swaps += cycle_size - 1
    
    return swaps

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output the minimum number of swaps
print(min_swaps_to_sort(arr))


'''

Sample Input :
5
1 5 4 3 2
Sample Output :
2

'''