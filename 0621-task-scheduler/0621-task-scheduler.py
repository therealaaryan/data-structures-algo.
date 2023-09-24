class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            if i not in count.keys():
                count[i] = 0
            count[i] += 1
        
        maxHeap = [-cnt for cnt in count.values()]
        
        heapq.heapify(maxHeap)
        
        time = 0
        
        q = []
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])
        
        return time