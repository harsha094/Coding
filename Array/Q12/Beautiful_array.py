def beautiful_array_sum(arr, n):
    # Initialize the sum = 0
    sum = 0
    # loop for adding sum
    for i in range(n):
        sum += arr[i]

    #check the sum is divisible by 2,3,5 or not
    if sum % 2 == 0 and sum % 3 == 0 and sum % 5 == 0:
        return 1
    else:
        return 0
# Input example
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array of heights

# Calculate the beautiful_array_sum
result = beautiful_array_sum(arr, n)
print(result)
