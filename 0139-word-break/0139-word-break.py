class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for c in wordDict:
                if i + len(c) <= len(s) and s[i: i + len(c)] == c:
                    dp[i] = dp[i + len(c)]
                
                if dp[i]:
                    break
        return dp[0]