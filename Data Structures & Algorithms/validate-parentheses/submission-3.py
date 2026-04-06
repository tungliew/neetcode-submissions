class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for op in s:
            if op in ["(", "[", "{"]:
                stack.append(op)
            elif op==")":
                if not stack or stack[-1]!="(":
                    return False
                stack.pop()
            
            elif op=="]":
                if not stack or stack[-1]!="[":
                    return False
                stack.pop()
            
            elif op=="}":
                if not stack or stack[-1]!="{":
                    return False
                stack.pop()
        
        
        return False if stack else True