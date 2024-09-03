n = int(input())
arr = list(map(int, input().split()))

largest_element = arr[0]
smallest_element = arr[0]
largest_index = 0
smallest_index = 0
# to find the indics of element 
for i, item in enumerate(arr):
    if item < smallest_element:
        smallest_element = item
        smallest_index = i  # Store index of new smallest element
    if item > largest_element:
        largest_element = item
        largest_index = i  # Store index of new largest element
# Calculate the difference between indices
index_difference = largest_index - smallest_index
#print the index_difference
print(index_difference)
'''
Sample Input :
5
1 6 4 0 3
Sample Output :
-2

'''