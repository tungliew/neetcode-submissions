class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect a cycle in graph

        graph = [[] for _ in range(numCourses)]

        for dest, src in prerequisites:
            graph[src].append(dest)

        # 0- unvisited, 1-visiting, 2-visited
        state = [0] * numCourses
        
        def dfs(course):
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            
            state[course]=1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            state[course]=2
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True