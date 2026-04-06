class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        used = [[False]*n for _ in range(m)]


        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            
            if grid[i][j]==0 or used[i][j]:
                return 0
            
            used[i][j] = True
            
            return (1
                + dfs(i+1, j)
                + dfs(i-1, j)
                + dfs(i, j+1)
                + dfs(i, j-1)
            )


        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not used[i][j]:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area
