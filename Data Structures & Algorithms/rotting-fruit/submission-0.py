class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        # bfs
        m , n = len(grid), len(grid[0])

        fresh = 0

        elapsed = 0

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh += 1
                elif grid[i][j]==2:
                    queue.append((i,j))
        # up/down/left/right
        directions = [[-1,0], [0, -1], [0,1], [1,0]]
        
        while queue and fresh>0:
            q_len = len(queue)
            for _ in range(q_len):
                i, j = queue.popleft()
                # 4 directions
                for d_i, d_j in directions:
                    new_i = i + d_i
                    new_j = j + d_j
                    if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j]==1:
                        grid[new_i][new_j] = 2
                        fresh -= 1
                        queue.append((new_i, new_j))
            
            elapsed += 1


        return elapsed if fresh==0 else -1
            
            
                