def max_sub_array(arr):
    # By  Kadane’s Algorithm
    #Initialize variables
    current_max = arr[0]
    global_max = arr[0]
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # update the current max with current element alone or the current max plus the previous element
        current_max = max(arr[i], current_max + arr[i])
        # update the global max if current max is greater than global max
        global_max = max(global_max, current_max)

    return global_max

n = int(input())
arr = list(map(int, input().split()))
print(max_sub_array(arr))

'''
Sample Input :
5
1 2 3 -2 5
Sample Output :
9

'''