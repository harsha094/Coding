def topKelement(nums, k):
    # Count the frequency of each element
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    #Sort the dictionary keys by their frequency (values) in descending order
    sorted_list = sorted(freq, key=lambda x:freq[x], reverse=True)
    #Return the first 'k' elements
    return sorted_list[:k]

# Example Usage
nums = [1, 2, 2, 3, 3, 3]
k = 2
print(topKelement(nums, k))

'''

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]

'''