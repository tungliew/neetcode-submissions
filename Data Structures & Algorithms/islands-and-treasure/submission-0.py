class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        if not grid:
            return 
        
        m, n = len(grid), len(grid[0]) 

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647
        
        while queue:
            i, j = queue.popleft()

            for di, dj in directions:
                new_i, new_j = i+di, j+dj

                if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j]==INF:
                    grid[new_i][new_j] = grid[i][j] + 1
                    queue.append((new_i, new_j))