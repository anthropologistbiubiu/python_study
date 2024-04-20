
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        min = 0
        for index, price in enumerate(prices):
            if index == 0:
                dp[0] = 0
            else:
                if price > prices[index - 1]:
                    dp[index] = max(dp[index-1],prices[index] - prices[min])
                else:
                    dp[index] = dp[index-1]
                    if prices[index] < prices[min]:
                        min = index
        return dp[len(prices) - 1]

solution = Solution()
# print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([3,2,6,5,0,3]))

