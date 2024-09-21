def max_sum_consecutive(arr, n):
    #Initialize the max_sum with very small value
    max_sum = float('-inf')
    
    #Loop through array and calculate the sum of consecutive elements
    for i in range(n - 1):
        current_sum = arr[i] + arr[i+1]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

#inputs
n = int(input())
arr = list(map(int, input().split()))
#Print the output
print(max_sum_consecutive(arr, n))
'''

Sample Input :
5
1 5 6 8 3
Sample Output :
14

'''