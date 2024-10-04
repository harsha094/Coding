def count_ones(num):
    # Convert to binary representation, remove '0b' prefix
    binary_representation = bin(num)[2:]
    #convert to list
    arr = list(binary_representation)
    count = 0 #counter to count
    for i in range(len(arr)):
        if arr[i] == '1':
            count = count + 1
    print(count)
    
num = int(input())
count_ones(num)

'''
Sample Testcase :
INPUT
276
OUTPUT
3

'''