class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        inRecursion = set()
        
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[b].append(a)
        
        
        
        def isCycle(u):
            visited.add(u)
            inRecursion.add(u)
            
            for v in adj[u]:
                if v not in visited and isCycle(v):
                    return True
                elif v in inRecursion:
                    return True
            
            inRecursion.remove(u)
            return False
        
        
        
        for i in range(numCourses):
            if i not in visited and isCycle(i):
                return False
        
        return True