class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = L + 1
        profit = 0
        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R
                #R += 1
            profit = max(profit, prices[R] - prices[L])

        return profit

