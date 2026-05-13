class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price = prices[0]
        max_profit = 0

        #loop through daliy prices
        for price in prices:
            #find the min price avalable
            min_price = min(price, min_price)

            #check the profit at current price
            max_profit = max(price - min_price, max_profit)

        return max_profit