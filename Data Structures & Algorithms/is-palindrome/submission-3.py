import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowering string to same case
        s = s.lower()

        new_s = ""

        for char in s:
            if char not in string.punctuation and char != " ":
                new_s += char     

        if len(new_s) % 2 == 0:
            return (new_s[:len(new_s)//2] == new_s[len(new_s)//2:][::-1])
        else:
            return (new_s[:len(new_s)//2] == new_s[len(new_s)//2 + 1:][::-1])       
        