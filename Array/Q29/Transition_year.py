def find_transition_year(years, parties):
    # Combine years and parties into a list of tuples and sort them by year
    year_parties_pair = sorted(zip(years, parties))
    transition_year = []
    # Iterate through the sorted list and check for party transitions
    for i in range(1, len(year_parties_pair)): #start from second element
        if year_parties_pair[i][1] != year_parties_pair[i-1][1]: #compare current party from previous
            transition_year.append(year_parties_pair[i][0]) # append the transition year
    
    return transition_year
#input 
n = int(input())
years = list(map(int, input().split()))
parties = input().split()
result = find_transition_year(years, parties)
for year in result:
    print(year)
'''
Sample Input :
5
2004 1999 2019 2009 2014
JDU JDU CON JDU CON
Sample Output :
2014

'''