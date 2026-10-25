import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanWord = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(cleanWord)-1
        while left < right :
            if cleanWord[left]!=cleanWord[right]:
                return False
            left +=1 
            right-=1
        return True
        