class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # print(tokens)

        for char in tokens:
            # print(char)
            # print(stack)
            if char in "+-*/":
                ele_1 = int(stack.pop())
                ele_2 = int(stack.pop())

                match char:
                    case "+": 
                        stack.append(str(ele_1 + ele_2)) 
                        # break
                    case "-":
                        stack.append(str(ele_2 - ele_1))
                        # break
                    case "*":
                        stack.append(str(ele_1*ele_2))
                        # break
                    case "/":
                        stack.append(str(int(ele_2 / ele_1)))
                        # break
            else:
                stack.append(char)

        return int(stack.pop())