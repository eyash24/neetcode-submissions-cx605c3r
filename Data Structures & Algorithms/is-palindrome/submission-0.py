import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = string.ascii_letters + string.digits
        s = s.lower()
        forward_str = ""
        backward_str = ""

        for letter in s:
            if letter not in allowed:
                continue
            forward_str += letter
            backward_str = letter + backward_str
        
        if forward_str == backward_str:
            return True
        else:
            return False