class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        ans = []
        
        def dfs(i, total):
            if total >= target or i >= len(candidates):
                if total == target:
                    ans.append(subset.copy())
                
                return
            
            subset.append(candidates[i])
            dfs(i, total + candidates[i])
            
            subset.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        
        return ans