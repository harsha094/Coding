import sys
#read all data input
input = sys.stdin.read
data =  input().strip().split('\n')

#read the number of array
k = int(data[0])
#Initialize a list to store sorted elements from all array 
all_element = []

#Read each array, sort it, and add it the the all_element array
index = 1
for _ in range(k):
    # Read the size of the current array (not actually used in processing)
    size = int(data[index])
    # Read the elements of the current array and convert them to integers
    arr_elements = list(map(int, data[index + 1].split()))
    #Sort the element
    arr_elements.sort()
    #add the element to the all_element array
    all_element.extend(arr_elements)
    #Move to the next array's data
    index += 2

#print all sorted array concatenated
print(" ".join(map(str, all_element)))

'''
Sample Input :
3
2
98 12
6
1 2 3 8 5 9
1
11
Sample Output :
12 98 1 2 3 5 8 9 11
'''