# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        
        stack = [(root, 1)]
        
        while stack:
            cur, depth = stack.pop()
            
            ans = max(ans, depth)
            
            if cur.right:
                stack.append((cur.right, depth + 1))
            
            if cur.left:
                stack.append((cur.left, depth + 1))
        
        return ans
            