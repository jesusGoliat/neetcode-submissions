from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1,len(prices)):
            if sell > prices[i]:
                profit += sell - buy
                buy = sell = prices[i]
            else:
                sell = prices[i]
        profit += sell - buy
        
        return profit