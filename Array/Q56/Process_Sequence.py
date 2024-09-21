def process_sequence(n, arr):
    result = []
    temp = [] #temp variable
    zero_found = False

    for num in arr:
        if num == 0:
            if zero_found:
                result.extend(temp)
                temp = []
            else:
                zero_found = True
                temp = []
        elif zero_found:
            # Collect numbers after the first zero
            temp.append(num)
     # If no result was collected after two zeros, return -1
    return result if result else [-1]

n = int(input())
sequence = list(map(int, input().split()))

# Process the sequence and print the result
output = process_sequence(n, sequence)
print(*output)



'''
Sample Testcase :
INPUT
10
1 1 1 0 1 0 1 1 0 1
OUTPUT
1 1 1
'''