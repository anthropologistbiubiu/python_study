
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)
        for index,price in enumerate(prices):
            if index == 0:
                dp[0] = 0
            if price > prices[index-1]:
                dp[index] = max(dp[index-0]+price,)


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
