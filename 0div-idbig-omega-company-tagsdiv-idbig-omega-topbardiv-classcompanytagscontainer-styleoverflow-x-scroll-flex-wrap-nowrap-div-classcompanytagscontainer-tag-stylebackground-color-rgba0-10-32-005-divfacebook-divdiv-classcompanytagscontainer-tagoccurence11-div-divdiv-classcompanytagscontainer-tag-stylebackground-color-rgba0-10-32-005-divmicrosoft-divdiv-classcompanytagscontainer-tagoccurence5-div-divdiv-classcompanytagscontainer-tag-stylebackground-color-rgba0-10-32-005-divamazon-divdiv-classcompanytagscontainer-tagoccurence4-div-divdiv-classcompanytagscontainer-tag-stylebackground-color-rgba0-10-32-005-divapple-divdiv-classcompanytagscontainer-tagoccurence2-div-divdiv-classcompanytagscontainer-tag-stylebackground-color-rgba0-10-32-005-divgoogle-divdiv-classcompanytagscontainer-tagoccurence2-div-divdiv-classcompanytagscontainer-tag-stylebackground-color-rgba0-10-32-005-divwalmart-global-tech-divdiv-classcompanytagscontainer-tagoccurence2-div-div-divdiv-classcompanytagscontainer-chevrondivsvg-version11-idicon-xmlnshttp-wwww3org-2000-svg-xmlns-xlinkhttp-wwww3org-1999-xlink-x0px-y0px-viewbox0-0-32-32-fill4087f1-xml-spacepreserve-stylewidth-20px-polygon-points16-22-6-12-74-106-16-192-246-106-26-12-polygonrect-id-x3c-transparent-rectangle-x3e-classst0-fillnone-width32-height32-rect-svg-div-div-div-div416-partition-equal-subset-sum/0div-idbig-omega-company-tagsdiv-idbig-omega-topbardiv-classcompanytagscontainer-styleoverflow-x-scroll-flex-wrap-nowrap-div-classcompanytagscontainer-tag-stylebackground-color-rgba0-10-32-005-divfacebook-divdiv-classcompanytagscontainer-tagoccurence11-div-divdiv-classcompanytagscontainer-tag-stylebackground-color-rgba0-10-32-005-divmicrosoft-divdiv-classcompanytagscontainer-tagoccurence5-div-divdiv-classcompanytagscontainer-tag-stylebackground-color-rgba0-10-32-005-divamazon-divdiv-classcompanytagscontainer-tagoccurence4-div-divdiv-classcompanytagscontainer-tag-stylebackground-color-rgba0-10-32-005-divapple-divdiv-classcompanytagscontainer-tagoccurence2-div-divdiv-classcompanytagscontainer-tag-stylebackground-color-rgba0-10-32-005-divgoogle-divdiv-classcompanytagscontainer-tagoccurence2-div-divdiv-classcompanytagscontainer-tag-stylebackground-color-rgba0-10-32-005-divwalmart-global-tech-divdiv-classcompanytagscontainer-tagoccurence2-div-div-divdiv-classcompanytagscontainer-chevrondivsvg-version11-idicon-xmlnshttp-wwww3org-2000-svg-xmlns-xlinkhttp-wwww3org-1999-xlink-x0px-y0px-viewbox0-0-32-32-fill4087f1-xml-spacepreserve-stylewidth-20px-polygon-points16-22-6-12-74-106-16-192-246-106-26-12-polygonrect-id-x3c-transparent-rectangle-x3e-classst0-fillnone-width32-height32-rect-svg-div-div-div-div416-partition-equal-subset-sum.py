class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for i in nums:
            dupDp = dp.copy()
            
            for t in dp:
                if i + t == target:
                    return True
                
                dupDp.add(i + t)
            dp = dupDp
        
        if target in dp:
            return True
        
        return False