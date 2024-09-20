def rotation_by_two_place(str1, str2):
    # Check if length of both strings is the same
    if len(str1) != len(str2):
        return 0
    # rotate left by two place in string 1 
    left_rotate = str1[2:] + str1[:2]
    #rotate right by two place in str str1
    right_rotate = str1[-2:] + str1[:-2]
    
    #Check if either of the rotations matches String 2 
    if str2 == left_rotate or str == right_rotate:
        return 1 
    else:
        return 0
        
#inputs        
str1 = input().strip()
str2 = input().strip()
print(rotation_by_two_place(str1, str2))

'''

Sample Input :
amazon
azonam
Sample Output :
1

'''