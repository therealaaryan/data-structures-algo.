class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        l = 0
        count = 0

        for r in range(len(s)):
            if s[r] not in d.keys():
                d[s[r]] = 0
            d[s[r]] += 1

            win_len = (r - l + 1)

            m = max(d.values())

            if win_len - m <= k:
                count = win_len
            
            else:
                d[s[l]] -= 1
                l += 1
            
            ans = max(ans, count)
        
        return ans