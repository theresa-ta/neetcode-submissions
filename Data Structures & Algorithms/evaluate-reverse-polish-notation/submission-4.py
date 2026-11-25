class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        for char in tokens:
            if char not in operators:
                stack.append(int(char))

            else:
                b = stack.pop()
                a = stack.pop()
                if char == "+":
                    value = a + b
                elif char == "-":
                    value = a - b
                elif char == "*":
                    value = a * b
                else:
                    value = int(a/b)
                stack.append(value)
        
        return stack[-1]