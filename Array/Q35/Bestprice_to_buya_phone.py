n = int(input())
arr = list(map(int, input().split()))
best_price = min(arr) # find the minimum in array
dealer = [] #Initialize an empty list to store the index of bestprice
for i in range(n):
    if arr[i] == best_price:
        dealer.append(str(i))
        
print("Dealer" + "".join(dealer))

'''

Sample Input :
3
10000 11200 12030
Sample Output :
Dealer0

'''