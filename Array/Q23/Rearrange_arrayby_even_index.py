def rearrange_array(arr):
    n = len(arr)
    #extract the even indexed array
    even_indexed_array = [arr[i] for i in range(n) if i % 2 == 0]

    #sort the even indexed array in asecending order
    even_indexed_array.sort()

    # rebuild the array, replace even indexed element with sorted ones
    even_index = 0
    for i in range(n):
        if i % 2 == 0:
            arr[i] = even_indexed_array[even_index]
            even_index += 1
    # print the modified array
    print(" ".join(map(str, arr)))

#input 
n = int(input())
arr = list(map(int, input().split()))
rearrange_array(arr)

'''
Sample Input :
5
3 9 1 44 6
Sample Output :
1 9 3 44 6
'''