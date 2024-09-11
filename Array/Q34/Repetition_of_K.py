# input the size and K 
n,k = map(int,input().split())
# Input the N elements in the list
elements = list(map(int, input().split()))

if k not in elements:
    print(-1)
else:
    #count the total occurence of k
    total_occurrence = elements.count(k)
    # K appears 1 time only i.e not in repetition
    if total_occurrence == 1:
        print("0")
    else:
        #if K appears more than onces, calculate how many times it repeat
        # Subtract 1 from total occurrences (as the first occurrence doesn't count as a repeat)
        print(total_occurrence - 1)

'''
Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0
'''