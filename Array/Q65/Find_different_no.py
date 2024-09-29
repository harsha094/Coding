def find_different_number(arr):
    if len(arr) < 3:
        return -1 #Not enough elements to determine series
    # Determine if series is mostly even or odd
    even_count = sum(1 for num in arr[:3] if num % 2 == 0)
    is_even_series = even_count >= 2

    #find different number 
    for num in arr:
        if is_even_series and num % 2 != 0:
            return num
        elif not is_even_series and num % 2 == 0:
            return num
    
    return -1 #no different number found

n = int(input())
arr = list(map(int, input().split()))
result = find_different_number(arr)
print(result)


'''
Sample Testcase :
INPUT
5
1 3 4 5 7
OUTPUT
4
'''