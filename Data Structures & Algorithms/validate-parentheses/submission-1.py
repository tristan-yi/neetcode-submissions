class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {")":"(", "}":"{", "]":"["}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                if stack[-1] != check[ch]:
                    return False
                stack.pop()
        
        return not stack
            
            
        