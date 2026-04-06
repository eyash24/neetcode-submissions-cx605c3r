class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in '({[':
                stack.append(char)

            elif char in ')}]':
                if len(stack):
                    if stack.pop() == parenthesis[char]:
                        continue
                    else:
                        return False
                else:
                    return False
                    
        if len(stack):
            return False
        return True
                    
        
        