class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = s.lower()
        lt = t.lower()
        first = list(ls)
        second = list(lt)
        if sorted(first) == sorted(second):
            return True 
        else:
            return False
