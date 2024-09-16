def max_frequency(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    max_count = max(freq.values())
    maximum_frequency_element = []
    for i, count in freq.items():
        if count == max_count:
            maximum_frequency_element.append(str(i))
        
    print(" ".join(maximum_frequency_element))

n = int(input())
arr = list(map(int, input().split())) 
max_frequency(arr)

'''
Sample Input :
7
1 2 3 4 4 4 5
Sample Output :
4

'''