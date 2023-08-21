# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        cur = root
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            
            if prev:
                if prev.val >= cur.val:
                    return False
            prev = cur
            cur = cur.right
        
        return True