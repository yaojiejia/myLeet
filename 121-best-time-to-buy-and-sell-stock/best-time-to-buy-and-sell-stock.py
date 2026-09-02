class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        profits = []
        buy = 0
        sell = 1 
        for i in range(len(prices)):
            if sell <= len(prices) - 1:
                if prices[sell] < prices[buy]:
                    buy = sell
                    sell = sell + 1 
                else:
                    profit = prices[sell] - prices[buy] 
                    profits.append(profit) 
                    sell += 1 
        
        if profits:
            return max(profits)
        else:
            return 0
        
