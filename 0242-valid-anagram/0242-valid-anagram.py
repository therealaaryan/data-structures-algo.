class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}

        for i in s:
            if i not in d_s.keys():
                d_s[i] = 0
            d_s[i] += 1
        
        for i in t:
            if i not in d_t.keys():
                d_t[i] = 0
            d_t[i] += 1
        
        return d_s == d_t