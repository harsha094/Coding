n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = []
# loop through array to fing consecutive difference
for i in range(n):
    # finding next index in consecutive and circular motion
    next_index = (i+1) % n
    # finding the absolute difference by abs() function because it's always give non-negative integer
    difference = abs(arr[i] - arr[next_index])
    #comparing with m to see if it's greater than print 1 otherwise 0
    if difference > m:
        result.append("1")
    else:
        result.append("0")
        
#print thr result
print(" ".join(result))

# Sample Input :
# 5 15
# 50 65 85 98 35
# Sample Output :
# 0 1 0 1 0