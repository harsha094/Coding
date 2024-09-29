def compare_string(s1, s2):
    if len(s1) != len(s2):
        print('no')
        return
    # loop for character by character
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print('no')
            return
        
    # return yes if loop completes without difference
    print('yes')

s1, s2 =map(str, input().split())
compare_string(s1, s2)

'''
Sample Testcase :
INPUT
guvi guvi
OUTPUT
yes

'''