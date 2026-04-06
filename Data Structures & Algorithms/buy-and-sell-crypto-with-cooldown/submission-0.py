class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]
        sell = 0
        cool = 0

        for i in range(1, len(prices)):
            prev_buy = buy
            prev_sell = sell
            prev_cool = cool

            buy = max(prev_buy, prev_cool-prices[i])
            sell = prev_buy + prices[i]
            cool = max(prev_cool, prev_sell)

        
        return max(sell, cool)
