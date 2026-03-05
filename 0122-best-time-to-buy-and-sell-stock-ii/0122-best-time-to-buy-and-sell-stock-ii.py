class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10e9
        profit = 0
        for r in range(1, len(prices)):
            if prices[r-1] < prices[r]:
                profit += (prices[r] - prices[r - 1])
        return profit