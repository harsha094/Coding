def rearrange_array(arr, n):
    #Initailize an empty array to store the rearrange number
    rearrange_arr = [0]*n 
    
    # Populate the result array
    for i in range(n):
        rearrange_arr[i] = arr[arr[i]]

    #print the rearrange_array
    print(" ".join(map(str, rearrange_arr)))
    
#inputs
n = int(input())
arr = list(map(int, input().split()))
rearrange_array(arr, n)

'''
Sample Input :
5
4 0 2 1 3
Sample Output :
3 4 2 0 1

'''