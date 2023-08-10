class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return t
            
        ds = {}
        dt = {}
        ans = ""
        tracker = float('inf')
        for i in t:
            if i not in dt.keys():
                dt[i] = 0
            dt[i] += 1
        
        for i in list(dt.keys()):
            ds[i] = 0
        
        l = 0
        
        count = 0

        for r in range(len(s)):
            if s[r] in ds.keys():
                ds[s[r]] += 1
                if ds[s[r]] == dt[s[r]]:
                    count += 1
            
            while count == len(dt):
                if (r - l + 1) < tracker:
                    tracker = (r - l + 1)
                    ans = s[l : r + 1]
                
                if s[l] in ds.keys():
                    ds[s[l]] -= 1
                    if ds[s[l]] < dt[s[l]]:
                        count -= 1
                l += 1
            
        return ans
            
            
        