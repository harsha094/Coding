n, ramesh_mark = map(int, input().split())
arr = list(map(int, input().split()))
# Initializing an empty list to store index
index_of_same = []
#loop to check the marks
for marks in arr:
    if marks == ramesh_mark:
        s = arr.index(marks)
        index_of_same.append(str(s))
#print the result
if index_of_same:
    print(" ".join(index_of_same))
else:
    print(-1) #if no such marks exist print -1

'''
Sample Input :
2 10
1 2
Sample Output :
-1

'''