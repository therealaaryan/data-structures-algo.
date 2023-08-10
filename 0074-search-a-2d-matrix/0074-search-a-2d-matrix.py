class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bot = row - 1
        r_ = 0
        while top <= bot:
            r_ = (top + bot) // 2

            if matrix[r_][-1] < target:
                top = r_ + 1
            
            elif matrix[r_][0] > target:
                bot = r_ - 1
            
            else:
                break
        
        if not(top <= bot):
            return False
        
        l = 0
        r = col - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[r_][mid] < target:
                l = mid + 1
            
            elif matrix[r_][mid] > target:
                r = mid - 1
            
            else:
                return True
        
        return False
