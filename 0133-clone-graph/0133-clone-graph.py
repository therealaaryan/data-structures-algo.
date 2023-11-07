"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            clone = Node(node.val)
            oldToNew[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        if not node:
            return None
        
        return dfs(node)