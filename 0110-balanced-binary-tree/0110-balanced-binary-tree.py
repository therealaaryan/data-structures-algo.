# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        heights = {}
        stack = [(root, False)]
        
        while stack:
            cur, visited = stack.pop()
            
            if cur:
                if visited:
                    l_height = heights.get(cur.left, 0)
                    r_height = heights.get(cur.right, 0)
                    
                    heights[cur] = 1 + max(l_height, r_height)
                    
                    if abs(l_height - r_height) > 1:
                        return False
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        
        return True