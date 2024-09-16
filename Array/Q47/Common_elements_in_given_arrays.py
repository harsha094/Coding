def common_element(arr1, arr2, n):
    i, j = 0, 0 #two pointers
    common_ele = []
    while i < n and j < n:
        if arr1[i] == arr2[j]:
            #If it's a common element, check if it's not a duplicate in the result
            if not common_ele or common_ele[-1] != arr1[i]:
                common_ele.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1 # move pointer to arr1
        else:
            j += 1 # move pointer to arr2
    if common_ele:
        print(" ".join(map(str, common_ele)))
    else:
        print('-1')

# Input
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Call the function
common_element(arr1, arr2, n)

'''
Sample Testcase :
INPUT
5
1 1 1 1 1
1 2 3 4 5
OUTPUT
1

'''