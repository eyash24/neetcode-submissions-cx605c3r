class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ["{","(","["]:
                stack.append(i)
            elif i in ["}",")","]"]:
                if stack:
                    ele = stack.pop()
                    if (i == "]" and ele =="[") or (i == ")" and ele =="(") or (i == "}" and ele =="{"):
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False