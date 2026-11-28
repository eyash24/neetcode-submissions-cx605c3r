from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = ''
        valid = ascii_letters + digits

        for l in s:
            if l in valid:
                strs += l
        

        if strs == strs[::-1]:
            return True
        else:
            return False
