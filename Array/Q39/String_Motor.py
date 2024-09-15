def solution(s, k):
    n = len(s)
    if not 0 <= k < n:
        return "Invalid input: k should be between 0 to len(s) - 1"
    
    #calculate effective rotation
    k = k % n

    # if k = 0, no rotation
    if k == 0:
        return s
    # perform rotation
    return s[k:] + s[:k]

s = input().strip()
k = int(input().strip())
result = solution(s, k)
print(result)

'''
Evaluation Parameters:
Sample Input
doselect
2 
Sample Output
selectdo

'''