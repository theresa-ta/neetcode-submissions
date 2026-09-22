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