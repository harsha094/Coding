n = int(input())
sum = 0
while n!=0:
    remainder = n % 10
    sqr = remainder * remainder
    sum = sum + sqr
    n = int(n/10)
    
print(sum)

'''
Sample Testcase :
INPUT
12
OUTPUT
5
'''