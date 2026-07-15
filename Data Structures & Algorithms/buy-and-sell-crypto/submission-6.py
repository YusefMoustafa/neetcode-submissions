class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # prices = [10,1,5,6,7,1]
        #              L
        #                      R
 
        L = 0
        R = L + 1
        profit = 0

        while R < len(prices):
            if prices[L] <= prices[R]:
                profit = max(profit, prices[R] - prices[L])
            else:

                L = R
            R += 1
            

        return profit
