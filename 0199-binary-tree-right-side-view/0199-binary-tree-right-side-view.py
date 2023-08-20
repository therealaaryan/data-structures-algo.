# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        
        ans = []
        
        while queue:
            limit = len(queue)
            for i in range(limit):
                cur = queue.pop(0)
                
                if i == limit - 1:
                    ans.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
        return ans
        