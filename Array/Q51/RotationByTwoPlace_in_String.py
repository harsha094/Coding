def rotation_by_two_place(str1, str2):
    # Check if length of both strings is the same
    if len(str1) != len(str2):
        return 0
    
    # Left Rotation using Stack
    stack_left = list(S1[:2])  # First 2 characters
    left_rotated = S1[2:] + ''.join(stack_left)  # Remaining + first 2 characters

    # Right Rotation using Stack
    stack_right = list(S1[-2:])  # Last 2 characters
    right_rotated = ''.join(stack_right) + S1[:-2]  # Last 2 characters + remaining

            # Above is using stack AND Below is without stack

    # rotate left by two place in string 1 
    left_rotated = str1[2:] + str1[:2]
    #rotate right by two place in str str1
    right_rotated = str1[-2:] + str1[:-2]
    
    #Check if either of the rotations matches String 2 
    if str2 == left_rotated or str == right_rotated:
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