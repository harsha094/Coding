def find_occurrence(arr, ques_arr):
    freq ={}
    #count the frequence of number in array
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    #For each number in ques_arr, check its frequency
    number_present = []
    for num in ques_arr:
        if num in freq:
            number_present.append(str(freq[num])) #append the frequency present
        else:
            number_present.append("Not Present") # append Not present if frequency is not present
    
    print(" ".join(number_present))

n = int(input())
arr = list(map(int, input().split()))
t = int(input())
ques_arr = list(map(int, input().split()))

find_occurrence(arr, ques_arr)

'''
Sample Input :
10
1 1 1 2 2 2 3 8 9 7
5
1 2 3 0 5
Sample Output :
3 3 1 Not Present Not Present

'''