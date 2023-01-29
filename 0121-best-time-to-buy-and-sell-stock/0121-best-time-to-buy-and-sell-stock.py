class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = float("inf")
        for i in prices:
            mini = min(mini,i)
            profit = max(profit,i - mini)
        return profit
            
        