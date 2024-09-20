m, n = map(int, input().split())  # Read the matrix dimensions
matrix_elements = list(map(int, input().split()))  # Read all the matrix elements in one line
target = int(input())  # Read the target element

# Check if the target is in the matrix
if target in matrix_elements:
    print("yes")
else:
    print("no")


'''

Sample Input :
2 5
2 3 0 7 1 5 3 4 1 8
11
Sample Output :
no

'''