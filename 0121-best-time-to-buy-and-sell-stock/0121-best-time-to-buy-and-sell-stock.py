class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0

        for r in range(len(prices)):
            ans = max(ans, (prices[r] - prices[l]))

            if prices[r] < prices[l]:
                l = r
        
        return ans