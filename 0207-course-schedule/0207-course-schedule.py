class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = [0]*numCourses

        for a, b in prerequisites:
            adj[b].append(a)

        def is_cyclic(v):
            if visited[v] == 1:
                return True
            if visited[v] == 2:
                return False

            visited[v] = 1
            if any(is_cyclic(neigh) for neigh in adj[v]):
                return True
            visited[v] = 2
            return False

        if any(is_cyclic(v) for v in range(numCourses)):
            return False

        return True