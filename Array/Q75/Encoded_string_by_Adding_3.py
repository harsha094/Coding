def encode_string(s):
    encoded_string = ""
    for char in s:
        # Shift character by 3 positions with wrap-around for uppercase letters
        if 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            encoded_string += new_char
    return encoded_string

s = input()
res = encode_string(s)
print(res)
'''
Sample Testcase :
INPUT
RADAR
OUTPUT
UDGDU

'''