class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = 0
        rob2 = 0
        
        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        
        
#         if len(nums) == 1:
#             return nums[0]
#         for i in range(len(nums)):
#             if i == 0 or i == 1:
#                 continue
            
#             nums[i] = nums[i] + nums[i - 2]
        
#         return max(nums[-1], nums[-2])


    