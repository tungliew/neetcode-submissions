class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        # used to check whether the grid is used
        used = [[False]*n for _ in range(m)]

        
        # check different conditions
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j]=="0" or used[i][j]:
                return
            
            used[i][j] = True

            # check 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not used[i][j]:
                    dfs(i, j)
                    count += 1

        return count
            
            