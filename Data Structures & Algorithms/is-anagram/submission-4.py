class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        for l in s:
            d1[l] = d1.get(l, 0) + 1
        
        for l in t:
            d2[l] = d2.get(l, 0) + 1
        
        if d1 == d2:
            return True 
        
        return False
