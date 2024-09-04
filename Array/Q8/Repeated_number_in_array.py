def find_the_repeated_twice(arr):
    ones = 0
    twos = 0
    for i in arr:
        # Update 'twos' with the bits that have appeared twice
        twos = twos | (ones & i)
        # Update 'ones' with the bits that have appeared once
        ones = ones ^ i
        # Get the common bits between 'ones' and 'twos'
        common_bits = ~(ones & twos)
        # Remove the bits that have appeared three times from 'ones' and 'twos'
        ones = ones & common_bits
        twos = twos & common_bits

        # The number that has appeared twice will be in 'twos' at the end
    return twos

n = int(input())
arr = list(map(int, input().split()))
print(find_the_repeated_twice(arr))
'''
Sample Input :
5
13 12 13 12 13
Sample Output :
12
'''