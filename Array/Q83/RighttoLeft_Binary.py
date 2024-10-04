def find_first_one_pos(num):
    # Convert to binary representation, remove '0b' prefix
    binary_representation = bin(num)[2:]

    # Reverse the binary repr to find the first '1' from right
    reversed_binary = binary_representation[::-1]

    # Find the index of the first '1' and 1 one for 1-based indexing
    position = reversed_binary.find('1') + 1

    return position

n = int(input())

print(find_first_one_pos(n))

'''
Sample Testcase :
INPUT
18
OUTPUT
2
'''