class Solution:

    # Method to encode a list of strings into a single string
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            # For each string, append its length, followed by '#', followed by the string itself
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    # Method to decode the encoded string back to a list of strings
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        
        # Process the encoded string
        while i < len(s):
            # Find the position of '#' to determine the length of the next string
            j = s.find('#', i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string based on the length
            decoded_list.append(s[j+1:j+1+length])
            # Move the pointer i to the next part
            i = j + 1 + length
            
        return decoded_list
'''

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

'''