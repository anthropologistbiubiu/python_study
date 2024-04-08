

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(len(dp)):
            print(i)
            if i == 0 or i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


solution = Solution()
print(solution.climbStairs(3))

