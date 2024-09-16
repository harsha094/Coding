def second_largest_element(arr):
    # sort array in descending order
    arr.sort(reverse=True)
    # start with second because first is largest element
    for i in range(1, len(arr)):
        # If the element is not equal to largest element
        if arr[i] != arr[0]:
            return arr[i]
        
    return "No second largest in Array"
    

n = int(input())
arr = list(map(int, input().split()))
print(second_largest_element(arr))


'''
Sample Input :
10
1 9 8 7 6 5 2 3 4 10
Sample Output :
9

'''