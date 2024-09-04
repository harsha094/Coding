def find_minimum(arr):
    smallest_element = arr[0] # initalize the smallest to arr[0] i.e first element
    #loop to iterate the array from second element
    for num in arr[1:]:
        if num < smallest_element:
            smallest_element = num
    return num



n = int(input())
arr = list(map(int, input().split()))
print(find_minimum(arr))

'''
Sample Input :
5
3 4 9 1 6
Sample Output :
1
'''