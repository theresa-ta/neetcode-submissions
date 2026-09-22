class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in "+-/*":
                stack.append(int(char))

            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if char == "+":
                    total = val2 + val1
                    stack.append(total)
                elif char == "-":
                    total = val2 - val1
                    stack.append(total)
                elif char == "*":
                    total = val2 * val1
                    stack.append(total)
                elif char == "/":
                    total = int(val2 / val1)
                    stack.append(total)

        return stack[0]
        
        
                

