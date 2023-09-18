class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for pair in points:
            x, y = pair
            
            d = (x**2) + (y**2)
            dist.append([d, x, y])
        
        heapq.heapify(dist)
        
        ans = []
        
        while k > 0:
            ele = heapq.heappop(dist)
            ans.append([ele[1], ele[2]])
            k -= 1
        
        return ans
        
        