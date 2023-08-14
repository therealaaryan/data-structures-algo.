class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float('inf')
        
        if nums[l] > nums[r]:
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] > nums[r]:
                    l = mid + 1
                
                else:
                    r = mid - 1
                    
                ans = min(ans, nums[mid])
        
        else:
            ans = nums[0]
        
        return ans