class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        maxx = 0
        for price in prices[1:]:
            profit  = price - lowest
            maxx = max(maxx,profit)
            lowest = min(lowest, price)
        return maxx    
