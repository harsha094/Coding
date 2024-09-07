def calculate_saving(n):
    #Initialize the saving of 1 month and initial saving
    saving = [1000, 1000]

    # loop to calculate saving of subsequent months
    for i in range(2, n+1): #inclusive 2 month to n
        next_month = saving[i-1] + saving[i-2]
        saving.append(next_month)

    #return the sum of saving
    return sum(saving)

n = int(input())
print(calculate_saving(n))
'''
Sample Input :
1
Sample Output :
2000

'''