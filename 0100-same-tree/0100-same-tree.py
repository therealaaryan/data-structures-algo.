# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            curP, curQ = stack.pop()
            
            if curP and curQ and curP.val == curQ.val:
                stack.append((curP.right, curQ.right))
                stack.append((curP.left, curQ.left))
            
            elif curP != curQ:
                return False
        
        return True