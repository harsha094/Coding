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

def calculate_air_encapsulated(arr):
    n = len(arr)
    #get the left max and right max height
    left_max, right_max = find_max_height(arr)
    #initialize the air to 
    total_air = 0
    #calculate air encapsulated at each position
    for i in range(n):
        air_at_i = min(left_max[i], right_max[i]) - arr[i]
        if air_at_i > 0:
            total_air += air_at_i

    return total_air

#input
n = int(input())
arr = list(map(int, input().split()))
#print result
print(calculate_air_encapsulated(arr))