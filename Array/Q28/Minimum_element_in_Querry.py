def process_query(queries):
    stored_list = [] #list to store element M
    result = [] # list to store result of '2'
    
    for query in queries:
        if query[0] == '1':
            stored_list.append(int(query[1]))
        elif query[0] == '2':
             # For '2', find and print the minimum element or -1 if the list is empty
            if stored_list:
                result.append(str(min(stored_list)))
            else:
                result.append('-1')
    
    #print result
    print(" ".join(result))

#input 
n = int(input()) # number of queries
queries = [input().split() for _ in range(n)] # read thye queries
process_query(queries)

'''

Sample Input :
5
1 60
2
1 58
2
1 69
Sample Output :
60 58

'''