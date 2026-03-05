class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10e9
        profit = 0
        for r in prices:
            lowest = min(lowest, r)
            profit = max(profit, r - lowest)
        
        return profit