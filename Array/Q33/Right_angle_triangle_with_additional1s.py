n = int(input())
# loop to iterate each level
for i in range(1, n+1):
    #count the ones needed for that level
    ones_count = 1+2*(i-1)
    #print the required number of ones
    print(" ".join(['1'] * ones_count))

'''
Sample Testcase :
INPUT
3
OUTPUT
1
1 1 1
1 1 1 1 1

'''