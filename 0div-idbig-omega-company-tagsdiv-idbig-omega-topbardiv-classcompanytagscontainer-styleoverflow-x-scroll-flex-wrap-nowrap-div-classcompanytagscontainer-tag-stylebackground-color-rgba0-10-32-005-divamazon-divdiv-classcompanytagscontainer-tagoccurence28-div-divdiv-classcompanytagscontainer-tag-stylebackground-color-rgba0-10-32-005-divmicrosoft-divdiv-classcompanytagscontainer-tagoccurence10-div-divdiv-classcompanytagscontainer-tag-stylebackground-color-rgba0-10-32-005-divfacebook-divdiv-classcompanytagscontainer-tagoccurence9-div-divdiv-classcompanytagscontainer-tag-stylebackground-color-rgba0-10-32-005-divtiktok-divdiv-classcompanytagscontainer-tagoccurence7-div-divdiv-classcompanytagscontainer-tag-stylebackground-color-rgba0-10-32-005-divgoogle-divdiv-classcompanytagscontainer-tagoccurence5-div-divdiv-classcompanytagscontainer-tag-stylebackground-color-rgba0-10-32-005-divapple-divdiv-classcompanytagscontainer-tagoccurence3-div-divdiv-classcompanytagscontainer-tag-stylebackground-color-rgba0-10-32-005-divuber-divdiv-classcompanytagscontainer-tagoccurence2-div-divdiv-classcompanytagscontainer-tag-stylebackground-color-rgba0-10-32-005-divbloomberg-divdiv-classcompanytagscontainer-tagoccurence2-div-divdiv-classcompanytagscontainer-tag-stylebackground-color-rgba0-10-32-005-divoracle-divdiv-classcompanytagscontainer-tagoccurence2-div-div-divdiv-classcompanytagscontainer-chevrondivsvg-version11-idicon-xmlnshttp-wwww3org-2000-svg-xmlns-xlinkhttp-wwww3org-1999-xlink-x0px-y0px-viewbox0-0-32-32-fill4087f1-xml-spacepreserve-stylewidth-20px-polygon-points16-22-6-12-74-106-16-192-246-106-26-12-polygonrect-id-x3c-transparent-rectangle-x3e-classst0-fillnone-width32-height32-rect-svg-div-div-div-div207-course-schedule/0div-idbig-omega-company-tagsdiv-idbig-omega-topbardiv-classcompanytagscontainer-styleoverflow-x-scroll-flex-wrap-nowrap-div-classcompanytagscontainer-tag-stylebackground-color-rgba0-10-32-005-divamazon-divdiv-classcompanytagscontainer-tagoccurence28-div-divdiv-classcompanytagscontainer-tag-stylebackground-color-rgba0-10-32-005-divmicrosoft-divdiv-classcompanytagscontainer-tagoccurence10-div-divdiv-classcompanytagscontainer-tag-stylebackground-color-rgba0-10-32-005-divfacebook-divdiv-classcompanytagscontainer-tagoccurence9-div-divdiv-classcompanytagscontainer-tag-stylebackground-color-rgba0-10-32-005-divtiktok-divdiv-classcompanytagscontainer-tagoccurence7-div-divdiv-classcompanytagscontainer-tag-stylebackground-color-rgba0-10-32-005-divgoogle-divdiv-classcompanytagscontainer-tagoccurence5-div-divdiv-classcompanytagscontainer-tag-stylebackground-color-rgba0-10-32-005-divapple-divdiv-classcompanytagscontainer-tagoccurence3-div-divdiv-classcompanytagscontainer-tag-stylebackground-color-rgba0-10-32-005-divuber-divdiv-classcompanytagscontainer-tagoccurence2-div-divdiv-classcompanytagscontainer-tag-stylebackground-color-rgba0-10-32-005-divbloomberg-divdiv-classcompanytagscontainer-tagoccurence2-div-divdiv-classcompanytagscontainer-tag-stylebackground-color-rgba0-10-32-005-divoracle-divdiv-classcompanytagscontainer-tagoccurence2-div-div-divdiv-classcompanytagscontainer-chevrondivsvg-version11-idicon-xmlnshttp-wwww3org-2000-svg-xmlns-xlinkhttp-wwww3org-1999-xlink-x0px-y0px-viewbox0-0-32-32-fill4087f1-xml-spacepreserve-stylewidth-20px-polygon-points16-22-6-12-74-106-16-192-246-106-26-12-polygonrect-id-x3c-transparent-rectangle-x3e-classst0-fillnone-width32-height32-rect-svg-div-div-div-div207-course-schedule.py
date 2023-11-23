class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = [0]*numCourses
        inRecursion = [0]*numCourses
        
        for a, b in prerequisites:
            adj[b].append(a)
        
        for i in range(numCourses):
            if not visited[i] and self.isCycleDFS(adj, i, visited, inRecursion):
                return False
        
        return True
    
    def isCycleDFS(self, adj, u, visited, inRecursion):
        visited[u] = True
        inRecursion[u] = True
            
        for v in adj[u]:
            if not visited[v] and self.isCycleDFS(adj, v, visited, inRecursion):
                return True
            elif inRecursion[v] == True:
                return True
            
        inRecursion[u] = False
        return False