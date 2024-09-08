def least_occurring_element(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # find minimum frequence
    minimum_freq = min(freq.values())
    
    #counting for least_occurring_element 
    least_occurring = []
    for num, count in freq.items():
        if count == minimum_freq:
            least_occurring.append(str(num))
            
    # sort in decreasing order
    least_occurring.sort(reverse = True)
    #print the least_occurring_element
    print(" ".join(least_occurring))

n = int(input())
arr = list(map(int, input().split()))
least_occurring_element(arr)



'''
Sample Input :
9
1 6 4 56 56 56 6 4 2
Sample Output :
2 1

'''