def delete_All_duplicate(arr):
    seen = set() # Set to track elements that have been added to the result
    result = [] # List to store the result

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return " ".join(result)

n = int(input())
arr = list(map(str, input().split()))
print(delete_All_duplicate(arr))

'''
Sample Input :
5
A23 B56 B56 C79 D16
Sample Output :
A23 B56 C79 D16

'''