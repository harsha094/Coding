n,w = map(int, input().split())
arr = list(map(int, input().split()))
#initalizing an empty list to store output
result = []
#loop for check through each window
for i in range(n-w+1):
    window = arr[i:i+w]
    #for no indexing
    found = False
    for j in range(w):
        if window[j] == 0:
            result.append(str(i+j+1)) # Append the 1-based index as a string
            found = True
            break
    # if no index with 0 than 
    if not found:
        result.append("-1")
        
#print the result
print(" ".join(result))

'''
Sample Input :
7 2
1 0 6 7 4 0 9
Sample Output :
2 2 -1 -1 6 6

'''