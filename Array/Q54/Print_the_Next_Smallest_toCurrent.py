def next_smaller_elements(arr, n):
    stack = []
    result = [-1]*n #Initialize the result array with -1
    #Traverse from right to left
    for i in range(n-1, -1, -1):
        # Remove elements from stack that are greater than or equal to the current element
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        
        #If stack is not empty, the top of the stack is the next smaller element
        if stack:
            result[i] = arr[stack[-1]]
        #push current indexd to the stack
        stack.append(i)
    return result

# Input handling
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array elements

# Call the function and print the result
output = next_smaller_elements(arr, n)
print(" ".join(map(str, output)))

''' 
Sample Input :
7
10 7 9 3 2 1 15
Sample Output :
7 3 3 2 1 -1 -1

'''