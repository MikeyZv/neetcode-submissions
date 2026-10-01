class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0

        res = 0
        for i in range(1,len(prices)):
            if prices[left] < prices[i]:
                profit = prices[i] - prices[left]
                if profit > res:
                    res = profit
            else:
                left = i

        return res

        