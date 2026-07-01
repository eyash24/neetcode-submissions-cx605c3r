from collections import Counter

class Solution:
    def checkValidString(self, s: str) -> bool:
        sc = Counter(s)

        if abs(sc['('] - sc[')']) > sc['*']:
            return False
        
        stars = []
        parenthesis = []

        for i in range(len(s)):
            if s[i] == '(':
                parenthesis.append(i)
            elif s[i] == ')':
                if parenthesis:
                    parenthesis.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            elif s[i] == '*':
                stars.append(i)

        if len(parenthesis) <= len(stars):
            while parenthesis:
                p_i, s_i = parenthesis.pop(), stars.pop()
                if p_i > s_i:
                    return False
            else:
                return True
        else:
            return False
        
