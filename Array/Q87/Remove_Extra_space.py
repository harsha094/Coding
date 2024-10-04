def remove_extra_space(sentence):
    result = [] #empty list to store sentence
    space_flag = False # Indicates if the last character was space or not

    for char in sentence:
        if char != ' ':
            result.append(char)
            space_flag = False # Reset the flag since it's not space
        elif not space_flag:
            result.append(' ') #add a single space
            space_flag = True # set the flag since the last character is space
    # convert the list to string and strip leading/trailing spce if any
    converted_string = ''.join(result).strip()
    return converted_string

S = input()
print(remove_extra_space(S))

#
#
#
#
'''
Sample Testcase :
INPUT
codekata challenge
OUTPUT
codekata challenge

'''