from collections import defaultdict
import sys

def maximumProfit(val, A, B):
    n = len(val)  # Number of cities
    m = len(A)    # Number of roads
    
    # Create a graph representation
    graph = defaultdict(list)
    for i in range(m):
        graph[A[i]].append(B[i])
    
    # Initialize variables to track maximum profit
    max_profit = -sys.maxsize
    
    # Perform DFS from each city
    def dfs(city, min_buy_price):
        nonlocal max_profit
        
        # Update max profit if possible
        if val[city-1] > min_buy_price:
            max_profit = max(max_profit, val[city-1] - min_buy_price)
        
        # Explore neighboring cities
        for neighbor in graph[city]:
            dfs(neighbor, min(min_buy_price, val[city-1]))
    
    # Start DFS from each city
    for city in range(1, n+1):
        dfs(city, val[city-1])
    
    return max_profit if max_profit != -sys.maxsize else -1

# Example usage:
# val = [2, 3, 1, 5]
# A = [1, 1, 2]
# B = [2, 3, 4]
# result = maximumProfit(val, A, B)
# print(result)  # Expected output: 3

'''
Evaluation Parameters

Sample Input
4
2
3
1
5
3
1
1
2
3
2
3
4
Sample Output
3
Explanation
The maximum profit of 3 rupees can be obtained as follows:

At City 1, buy paneer for 2 rupees
Traverse Road 1 to get to City 2
Traverse Road 2 to get to City 4
At City 4, sell the paneer for 5 rupees

'''