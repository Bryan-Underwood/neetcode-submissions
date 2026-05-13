class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price = float('inf')
        max_profit = 0

        #loop through daliy prices
        for price in prices:
            #find the min price avalable
            if price < min_price:
                min_price = price

            #check the profit at current price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit