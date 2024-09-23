def group_anagram(strs):
    #dictionary to hold group of anagram
    anagram_dict = []

    #loop through each string in input list
    for word in strs:
        #sort the characters in the string
        sorted_word = ''.join(sorted(word))

        #Use the sorted string as the key in the dictionary
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    # Return the grouped anagrams as a list of lists
    return list(anagram_dict.values())

# Test cases
strs1 = ["act", "pots", "tops", "cat", "stop", "hat"]
strs2 = ["x"]

print(group_anagram(strs1))
print(group_anagram(strs2))

'''

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]

'''