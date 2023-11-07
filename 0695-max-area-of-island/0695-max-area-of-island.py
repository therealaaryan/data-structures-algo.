class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0
        
        def traverse(i, j):
            if (i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == 0 or (i, j) in visited):
                return 0
            
            visited.add((i, j))
            return (1 + traverse(i + 1, j) +
                        traverse(i - 1, j) +
                        traverse(i, j + 1) +
                        traverse(i, j - 1))
        
        for i in range(rows):
            for j in range(cols):
                area = max(area, traverse(i, j))
        
        return area