# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = [root]
        
        while stack:
            cur = stack.pop()
            if self.sameTree(cur, subRoot):
                return True
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        
        return False
        
    def sameTree(self, root1, root2):
        stack = [(root1, root2)]
        
        while stack:
            cur1, cur2 = stack.pop()
            
            if cur1 and cur2 and cur1.val == cur2.val:
                stack.append((cur1.right, cur2.right))
                stack.append((cur1.left, cur2.left))
            
            elif cur1 != cur2:
                return False
        
        return True