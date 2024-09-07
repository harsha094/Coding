user_input = input()
n = len(user_input)
middle = n // 2 # Integer division to find the middle index
if n % 2 == 0:
    # For even length: replace the two middle elements
    replaced_str = user_input[:middle-1]+ "**" + user_input[middle+1:]
else:
    #For odd length: replace the middle element
    replaced_str = user_input[:middle]+ "*" + user_input[middle+1:]
print(replaced_str)
'''
Sample Testcase :
INPUT
hello
OUTPUT
he*lo

'''