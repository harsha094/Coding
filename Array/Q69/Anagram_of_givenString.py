def find_anagram(n, strings):
    target = 'kabali'
    
    # count the freq of each character in target
    target_count = {}
    for char in target:
        target_count[char] = target_count.get(char, 0) + 1
        
    anagram_count = 0
    # Iterate through each string in given list
    for string in strings:
        # count frequence of each charcter in  curent string 
        current_count = {}
        for char in string:
            current_count[char] = current_count.get(char, 0) + 1
            
        #Compare the current_count with target_count
        if current_count == target_count:
            anagram_count += 1
        
    return anagram_count

#inputs
n = int(input())
strings = []
for _ in range(n):
    strings.append(input().strip())

# find and print the number of anagram
result = find_anagram(n, strings)
print(result)

'''
Sample Testcase :
INPUT
5
kabali
kaabli
kababa
kab
kabail
OUTPUT
3
'''