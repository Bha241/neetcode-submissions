class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest = 0
        for char in s:
            if char in substring:
                substring = substring[substring.index(char) + 1:]
            substring += char
            longest = max(longest, len(substring))
        return longest
                
               
            


        