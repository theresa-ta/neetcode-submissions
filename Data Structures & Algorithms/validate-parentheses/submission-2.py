class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []

        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }

        for char in s:
            if char in pairs.keys():
                stack.append(char)
            
            if char in pairs.values():
                if len(stack) == 0:
                    return False
                if pairs[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        
        return False

        #added an empty stack list. created a dictionary where key must match value in this case its needed. 
        #then, we loop the string. if the string is an open bracket, add to stack. once we see a closing bracket, does it match the closest opening bracket? yes, remove. no, false. 
        #stack is important here because it pops the last value aka the top for stack