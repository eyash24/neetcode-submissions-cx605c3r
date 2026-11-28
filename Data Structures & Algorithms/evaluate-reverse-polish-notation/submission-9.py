class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))

            else:
                x1 = stack.pop()
                x2 = stack.pop()

                match t:
                    case '+': 
                        stack.append(x2+x1)                    
                    case '-':
                        stack.append(x2-x1)                     
                    case '*':
                        stack.append(x2*x1)                    
                    case '/':
                        stack.append(int(x2/x1))
        return stack[-1]                 
            

        



