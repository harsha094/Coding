n = int(input())
arr = list(map(int, input().split()))
k = int(input())
#an empty list to store the negative integers
result = []
# loop through array to check each window
for i in range(n - k + 1):
    window = arr[i:i+k]
    # Finding the first negative number in window
    found_negative = False
    for num in window:
        if num < 0:
            result.append(str(num))
            found_negative = True
            break
     # IF all numbers are positive    
    if not found_negative:
        result.append("0")
        
#print all result
print(" ".join(result))

# Sample Input :
# 7
# 1 -2 -3 -4 5 6 -7
# 3
# Sample Output :
# -2 -2 -3 -4 -7