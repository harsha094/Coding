def second_smallest_element(arr, n):
    arr.sort() #sort the array in ascending order
    #start with second index because first is smallest
    for i in range(1, n):
        # If the element is not equal to smallest element
        if arr[i] != arr[0]:
            return arr[i]
    
    return '-1'
        
    
n = int(input())
arr = list(map(int, input().split()))
print(second_smallest_element(arr, n))

'''
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
2
'''