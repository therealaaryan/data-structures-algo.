class Solution:
    def isValid(self, s: str) -> bool:
        d = {')' : '(', '}' : '{', ']' : '['}

        stack = []

        for i in s:
            if i in d.values():
                stack.append(i)
            
            if i in d.keys():
                if stack:
                    top = stack.pop()
                    if top != d[i]:
                        return False
                else:
                    return False
        
        if not stack:
            return True
        
        return False