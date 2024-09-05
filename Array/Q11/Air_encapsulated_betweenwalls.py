def find_max_height(arr):
    n = len(arr)
    # intialize the arrays to store left and right maximum height
    left_max = [0]*n
    right_max = [0]*n

    #compute for left
    left_max[0] = arr[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1], arr[i])

    #compute for right
    right_max[n-1] = arr[n-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])

    return left_max, right_max