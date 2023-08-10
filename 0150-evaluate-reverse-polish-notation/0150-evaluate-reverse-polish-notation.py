class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op= ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in op:
                if i == op[0]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                
                elif i == op[1]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                
                elif i == op[2]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                
                elif i == op[3]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            
            else:
                stack.append(int(i))
        
        return stack[0]