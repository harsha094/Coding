n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
#sort in ascending order 
arr1.sort()
#sort in descending order
arr2.sort(reverse = True)
#merging both array
f_array = arr1 + arr2
#printing final array : we use map(str, arr) here to convert the integer array to string
print(" ".join(map(str, f_array)))
'''
Sample Input :
3 3
23 15 16
357 65 10
Sample Output :
15 16 23 357 65 10

'''