def remove_vowels(s):
    chars = 'aeiouAEIOU'
    return ''.join([ch for ch in s if ch not in chars])
def reverse_string(S):
    return S[::-1]

S = input()
s = reverse_string(S)
result = remove_vowels(s)
if result:
    print(result)
else:
    print('-1')
    

'''
Sample Testcase :
INPUT
codekata
OUTPUT
tkdc

'''