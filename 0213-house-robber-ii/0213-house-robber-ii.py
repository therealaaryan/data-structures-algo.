class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        nums1 = nums[:len(nums) - 1]
        for i in nums1:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        nums2 = nums[1:]
        
        rob3 = 0
        rob4 = 0
        
        for i in nums2:
            temp = max(i + rob3, rob4)
            rob3 = rob4
            rob4 = temp
        
        return max(rob2, rob4, nums[0])