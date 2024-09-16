def count_string(str1, str2):
    
    count = 0 #Initialize an count 
    # Iterate through str1 to find the str2 content
    for i in str1:
        if i == str2:
            count += 1 
    # if no string 2 is found than print -1    
    if count:
        print(count)
    else:
        print(-1)
    

#Inputs
str1 = input().split() 
str2 = input()
count_string(str1, str2)


'''
Sample Testcase :
INPUT
I enjoy doing codekata
codekata
OUTPUT
1

'''