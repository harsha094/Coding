n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
#merge both the arrays
arr = arr1 + arr2
#sort the new array
arr.sort()
#print the sum of the middle two elements
print(arr[n]+arr[n-1])
'''
Sample Input :
5
1 9 16 25 46
2 3 4 5 6
Sample Output :
11

'''