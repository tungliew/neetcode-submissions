class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        target = total // 2

        n = len(stones)

        dp = [[0]*(target+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1,target+1):
                # doesn't in clude the current stone
                dp[i][j] = dp[i-1][j]

                if j>=stones[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-stones[i-1]]+stones[i-1])
        
        return total - 2 * dp[n][target]