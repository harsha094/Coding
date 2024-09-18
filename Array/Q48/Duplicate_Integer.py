class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using a set to track seen element
        seen = set()

        for num in nums:
            if num in seen:
                return True # If already in the set, duplicate found
            seen.add(num)
        return False # No duplicate found

'''

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

'''