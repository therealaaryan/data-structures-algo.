class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        lst = set()

        for r in range(len(s)):
            while s[r] in lst:
                lst.remove(s[l])
                l += 1

            lst.add(s[r])
            ans = max(ans, (r - l + 1))

        return ans 