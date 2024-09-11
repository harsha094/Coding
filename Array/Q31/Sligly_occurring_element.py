def find_singly_occurring_number(arr):
    freq = {}
    #Count the frequency of each number 
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    #find minimum in frequency
    minimum_freq = min(freq.values())
    #count the singly occurring element
    singly_occurring = []
    for i, count in freq.items():
        if count == minimum_freq:
            singly_occurring.append(str(i))

    # print the singly occurring element
    print(" ".join(singly_occurring))

#Input
n = int(input())
arr = list(map(int, input().split()))
find_singly_occurring_number(arr)

'''
Sample Input :
5
1 1 2 5 5
Sample Output :
2

'''