n = int(input())
arr = list(map(int, input().split()))

#check if n is greater or equal to 6 or not 
if n >= 6:
    # calculate the sum of first three number 
    first_three_sum = sum(arr[:3])
    #calculate the sum of last three number
    last_three_sum = sum(arr[-3:])
    
    # check for majestic
    if first_three_sum == last_three_sum:
        print(1)
    else:
        print(0)
# if array has less than 6 element it can't be majestic
else:
    print(0)

'''
Sample Input :
7
1 2 3 4 6 0 0
Sample Output :
1

'''