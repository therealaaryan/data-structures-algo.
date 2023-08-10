class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        l_max = height[l]
        r_max = height[r]
        ans = 0

        while l < r:
            if l_max < r_max:
                l += 1
                if (l_max - height[l]) > 0:
                    ans += l_max - height[l]
                l_max = max(l_max, height[l])
            
            else:
                r -= 1
                if (r_max - height[r]) > 0:
                    ans += r_max - height[r]
                r_max = max(r_max, height[r])

        return ans
                
        
