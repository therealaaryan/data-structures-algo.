class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def traverse(i, j):
            q = [(i, j)]
            while q:
                cur_i, cur_j = q.pop(-1)
                if (cur_i, cur_j) not in visited:
                    visited.add((cur_i, cur_j))
                    
                    for direction in directions:
                        next_i, next_j = cur_i + direction[0], cur_j + direction[1]
                        
                        if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][next_j] == "1": 
                            traverse(next_i, next_j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    traverse(i, j)
                    islands += 1
        
        return islands