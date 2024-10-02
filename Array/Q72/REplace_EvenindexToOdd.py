def swap_even_odd_characters(S):
    # convert string to list 
    chars = list(S)
    n = len(chars)
    # Iterate through the list in steps of 2
    for i in range(0, n-1, 2):
        #swap characters at index i and i+1
        chars[i], chars[i+1] = chars[i+1], chars[i]
    
    #join the list back to string
    return ''.join(chars)

#inputs
S = input()
#Output the result
print(swap_even_odd_characters(S))

'''
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat

'''