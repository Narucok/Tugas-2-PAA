from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        buy = -prices[0]  
        sell = 0          
        cooldown = 0      

        for price in prices[1:]:
            prev_buy = buy
            prev_sell = sell
            prev_cooldown = cooldown

            buy = max(prev_buy, prev_cooldown - price)
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_buy + price

        return max(sell, cooldown)
