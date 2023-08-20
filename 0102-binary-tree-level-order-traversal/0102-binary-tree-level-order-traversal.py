# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        
        while queue:
            sub = []
            limit = len(queue)
            for i in range(limit):
                cur = queue.pop(0)
                sub.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            ans.append(sub)
            
        
        return ans
            