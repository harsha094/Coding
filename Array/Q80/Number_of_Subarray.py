n = int(input())
arr = list(map(int, input().split()))
#by Sub_array Formula 
Number_of_Sub_array = n*(n+1)/2
print(Number_of_Sub_array)

'''
Sample Testcase :
INPUT
5
1 2 3 2 1
OUTPUT
15

'''