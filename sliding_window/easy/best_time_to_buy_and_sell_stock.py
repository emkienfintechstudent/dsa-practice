#link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpurchase = 100000
        maxprofit = 0 
        for i in prices:
            if i < minpurchase:
                minpurchase = i 
            maxprofit = max(maxprofit, i - minpurchase)
        return maxprofit