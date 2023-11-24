class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        l = 0
        r = len(piles) - 2
        ans = 0
        
        while l < r:
            ans += piles[r]
            l += 1
            r -= 2
        
        return ans