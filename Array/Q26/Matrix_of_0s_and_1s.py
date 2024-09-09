m,n = map(int, input().split())
matrix = [] #Initialize the matrix
sita_count = 0 #variable to count the wining of Sita
ram_count = 0 #variable to count the wining of Ram
#loop to get the input in matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
    
#loop to iterate in matrix with condition to check for wining
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            sita_count += 1
        else:
            ram_count += 1

#print the Count of wining
print("RAM:",ram_count)
print("SITA:",sita_count)

'''
Sample Input :
1 3
1 1 1
Sample Output :
RAM: 0
SITA: 3

'''