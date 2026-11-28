class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        di = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for l in s:
            if l in ('{', '(', '['):
                stack.append(l)
            else:
                if l in (')', '}', ']'):
                    if stack:
                        ele = stack.pop()
                        if ele == di[l]:
                            continue
                        else:
                            return False
                    else:
                        return False
            
        if len(stack) > 0:
            return False
        else:
            return True