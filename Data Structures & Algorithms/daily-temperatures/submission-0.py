class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]
        temp = temperatures[::-1]
        stack = [temp[0]]
        stack_len = 1
        
        for t in temp[1:]:
            print()
            i = stack_len -1
            print(i)
            print(t)
            print(stack)
            while i >= 0 and stack[i] <= t:
                print(i)
                print(stack[i])
                i -= 1
            if i < 0 : res.append(0)
            else: res.append(stack_len -i)
            
            stack_len += 1
            stack.append(t)
        
        return res[::-1]