#Inputs
n = int(input())
arr = list(map(int, input().split()))
sum = 0 # to count sum
#Loop to iterate
for i in range(n - 1):
    #count the sums obtained by all consecutive pairs with sum
    sum = sum + arr[i] + arr[i+1]

#Print output 
print(sum)

'''Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
24((1+2)+(2+3)+(3+4)+(4+5))
'''
