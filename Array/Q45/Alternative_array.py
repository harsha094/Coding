def alternative_array(arr):
    #sort the array in ascending order
    arr.sort()
    #Initialize two pointer
    left = 0 # start from smallest element
    right = len(arr) - 1 # start from largest element
    
    #to store the result
    result = []
    # Build the alternative array
    while left <= right:
        if left <= right:
            result.append(arr[right]) # store the largest
            right -= 1
        if left <= right:
            result.append(arr[left]) #store the smallest
            left += 1
    #print the result
    print(*result)

#Inputs
n = int(input())
arr = list(map(int, input().split()))
alternative_array(arr)

'''
Sample Input :
5 1 7 11 16 19
Sample Output :
19 1 16 7 11

'''