def remove_imm_duplicate(str):
    res = []
    i = 0
    while i < len(str):
        # check if the current and next is same 
        if i+1 < len(str) and str[i] == str[i+1]:
            #skip both remove_imm_duplicate
            i += 2
        else:
            #append the current to res
            res.append(str[i])
            i += 1
            
    final_result = ''.join(res)
    return final_result if final_result else '-1'
    
input_string = input()
print(remove_imm_duplicate(input_string))

'''Sample Input :
1331
Sample Output :
11'''