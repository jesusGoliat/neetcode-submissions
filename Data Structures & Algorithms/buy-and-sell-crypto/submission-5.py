class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = buy = prices[0]
        for x in prices:
            if buy > x:
                profit = max(profit,sell - buy)
                sell = buy = x
            elif sell < x:
                sell = x
        profit = max(profit,sell-buy)
        return profit

