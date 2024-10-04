def binary_to_octal(num):
    # Convert binary string to an integer
    decimal_value = int(num, 2)
    # Convert the decimal value to octal
    octal_value = oct(decimal_value)[2:]
    return octal_value

num = input()
print(binary_to_octal(num))

'''
Sample Testcase :
INPUT
1100100
OUTPUT
144
'''