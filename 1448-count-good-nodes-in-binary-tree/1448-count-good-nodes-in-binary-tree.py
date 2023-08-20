# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        
        ans = 0
        
        while stack:
            cur, check = stack.pop()
            
            if cur.val >= check:
                ans += 1
                check = cur.val
            
            if cur.right:
                stack.append((cur.right, check))
            if cur.left:
                stack.append((cur.left, check))
        
        return ans