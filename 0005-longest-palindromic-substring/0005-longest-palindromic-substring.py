class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        anslen = 0
        
        for i in range(len(s)):
            l = i
            r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > anslen:
                    ans = s[l : r + 1]
                    anslen = (r - l + 1)
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > anslen:
                    ans = s[l : r + 1]
                    anslen = (r - l + 1)
                l -= 1
                r += 1
            
        return ans
            
            
                