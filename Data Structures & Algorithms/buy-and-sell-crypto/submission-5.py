class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        if len(prices) >= 2:
            right = 1
        else:
            return 0

        profit = 0     
        for i in range(len(prices)):
            bought = prices[i]
            for j in range(i+1,len(prices)):
                sold = prices[j]

                if sold - bought > profit:
                    profit = sold - bought

        if profit < 0:
            profit = 0

        return profit

        