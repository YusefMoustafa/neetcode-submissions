class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}':'{', ')':'(', ']':'['}

        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            
        if not stack:
            return True
        
        else:
            return False