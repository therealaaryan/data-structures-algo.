# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, False)]
        heights = {}
        ans = 0
        
        while stack:
            cur, visited = stack.pop()
            
            if cur:
                if visited:
                    l_height = heights.get(cur.left, 0)
                    r_height = heights.get(cur.right, 0)
                    
                    heights[cur] = max(l_height, r_height) + 1
                    
                    ans = max(ans, (l_height + r_height))
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return ans