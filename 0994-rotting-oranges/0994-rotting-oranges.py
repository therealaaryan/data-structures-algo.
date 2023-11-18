class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        
        q = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while fresh > 0 and q:
            length = len(q)
            
            for i in range(length):
                r, c = q.pop(0)
                
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1
            
            time += 1
            
        if fresh == 0:
            return time
            
        return -1