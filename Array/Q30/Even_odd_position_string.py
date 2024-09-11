user_input = input() #input 
n =len(user_input) # len of input 
# initializing two empty list to store even and odd positioned character
even_str =[]
odd_str = []
for i in range(n):
    if i % 2 == 0:
        even_str.append(user_input[i])
    else:
        odd_str.append(user_input[i])
        
print("".join(even_str), end=" ")
print("".join(odd_str))

'''
Sample Testcase :
INPUT
XCODE
OUTPUT
XOE CD

'''