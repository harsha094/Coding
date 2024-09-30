N, K = map(int, input().split())
#Initialize an count to count occurrence
count = 0
# loop to Take out the digits one by one in N 
while (N > 0):
    if (N % 10 == K):
        count += 1
    N = N // 10

if count:
    print(count)
else:
    print('-1')


'''
Sample Testcase :
INPUT
1000 0
OUTPUT
3
'''