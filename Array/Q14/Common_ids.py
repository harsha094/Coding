def find_common_ids(arr):
    freq = {}
    #Count the frequency of each id
    for id in arr:
        if id in freq:
            freq[id] += 1
        else:
            freq[id] = 1
    # counting for repeated ids 
    common_ids = [] #Initalizing a list to collect common ids
    for id, count in freq.items():
        if count > 1:
            common_ids.append(str(id)) # adding id in string format for easier printing later
        
    #printing the result
    if common_ids:
        print(" ".join(common_ids))
    else:
        print(-1)
        
n = int(input())
arr = list(map(int, input().split()))
find_common_ids(arr)

'''
Sample Input :
7
1 1 11 121 131 141 98
Sample Output :
1

'''