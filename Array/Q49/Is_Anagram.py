class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Initialize frequency dictionaries
        freq1 = {}
        freq2 = {}
        # count freq in each character in str1
        for char in s:
            freq1[char] = freq1.get(char, 0) + 1
        # count freq in each charcter in str2
        for char in t:
            freq2[char] = freq2.get(char, 0) + 1

        #compare frequency in dictionary
        return freq1 == freq2
        
        #Or another approach is sorting
        # return sorted(s) == sorted(t)

'''
Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

'''