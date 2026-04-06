class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for  t in tokens:
            if t in ["+","-","*","/"]:
                op2 = stack.pop()
                op1 = stack.pop()
                
                match t:
                    case "+": stack.append(op1+op2)
                    case "-": stack.append(op1-op2)
                    case "*": stack.append(op1*op2)
                    case "/": stack.append(int(op1/op2))
            else:
                stack.append(int(t))
        return int(stack[-1])
                    