class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        pac, atl = set(), set()
        
        def dfs(i, j, visit, prevHeight):
            if ((i, j) in visit or i < 0 or i == rows or j < 0 or j == cols or heights[i][j] < prevHeight):
                return
            
            visit.add((i, j))
            
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                
                if 0 <= next_i < rows and 0 <= next_j < cols and heights[next_i][next_j] >= prevHeight:
                    dfs(next_i, next_j, visit, heights[i][j])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        ans = []
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        
        return ans