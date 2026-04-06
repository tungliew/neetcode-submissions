class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land_count = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_count += 1
        
        
        # count the number of adjacent lands
        overlapped = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    # check right
                    if j+1<n and grid[i][j+1]==1:
                        overlapped += 1
                    # check down
                    if i+1<m and grid[i+1][j]==1:
                        overlapped += 1
        
        
        perimeter = land_count * 4 - overlapped * 2

        return perimeter
