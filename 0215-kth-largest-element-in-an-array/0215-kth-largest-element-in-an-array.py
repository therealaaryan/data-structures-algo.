class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = len(nums)
        n = 0
        
        heapq.heapify(nums)
        
        while n < l - k:
            heapq.heappop(nums)
            n += 1
        
        return heapq.heappop(nums)