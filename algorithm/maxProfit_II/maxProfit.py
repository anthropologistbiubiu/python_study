
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        max_profit = 0
        buy = 0
        for i in range (m-1):
            if prices[i] < prices[i+1]:
                buy = i
                break
                  
        dp = [0] * m
        for j in range(buy+1, m):
            dp[j] = max(dp[j-1], dp[j-1] + prices[j]-prices[j-1])
        return dp[m-1] 


solution = Solution()

print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,4,2]))
