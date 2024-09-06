m,n = map(int, input().split())# Read the number of rows (m) and columns (n)
matrix =[]
# Step 2: Input the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# flattened the matrix 
flattened_matrix = [item for row in matrix for item in row]
#Sort the flattened matrix 
flattened_matrix.sort()
#reshape the flattened matrix into 2D matrix
sorted_matrix = []
for i in range(m):
    sorted_matrix.append(flattened_matrix[i*n:(i+1)*n])

#print the sorted matrix
for row in sorted_matrix:
    print(" ".join(map(str, row))) 

'''
Sample Input :
3 3
87 21 34
89 32 78
12 23 45
Sample Output :
12 21 23
32 34 45
78 87 89

'''