n = input()
odd_number = []
for i in n:
    if int(i) % 2 != 0:
        odd_number.append(i)
        
if odd_number:
    print(" ".join(odd_number))
else:
    print(-1)

'''
Input Size : N <= 100000
Sample Testcase :
INPUT
2143
OUTPUT
1 3

'''