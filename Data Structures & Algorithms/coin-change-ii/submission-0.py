class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)

        dp = [[0]*(amount+1) for _ in range(m+1)]

        # base case
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(amount+1):
                # not including
                dp[i][j] = dp[i-1][j]
                # including
                if j>=coins[i-1]:
                    dp[i][j] = dp[i][j] +   (dp[i][j-coins[i-1]])


        return dp[m][amount]  