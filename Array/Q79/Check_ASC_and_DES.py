def check_sorted_or_not(arr, n):
    if n <= 1:
        # An array with 0 or 1 element is considered sorted.
        print("yes")
        return
    is_ascending = True
    is_descending = True
    
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            # If an element is greater than the previous one, it can't be descending.
            is_descending = False
        elif arr[i] < arr[i-1]:
            # If an element is less than the previous one, it can't be ascending.
            is_ascending = False
    # if either ascending or descending holds true print yes
    if is_ascending or is_descending:
        return 'yes'
    else:
        return 'no'

n = int(input())
arr = list(map(int, input().split()))
result = check_sorted_or_not(arr, n)
print(result)

'''
Sample Testcase :
INPUT
3
2 3 7
OUTPUT
yes

'''