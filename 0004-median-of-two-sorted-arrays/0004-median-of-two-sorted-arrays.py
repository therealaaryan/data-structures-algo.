class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) % 2 == 0:
            mid = (l + r) // 2
            
            ans = (nums[mid + 1] + nums[mid]) / 2
            
            return ans
        else:
            mid = (l + r) // 2
            ans = nums[mid]
            return ans
        
        