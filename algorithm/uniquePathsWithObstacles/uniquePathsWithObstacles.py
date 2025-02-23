from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range (m):
            for j in range (n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] =1 
                        continue
                    else:
                        return 0
                if obstacleGrid[i][j] == 0:
                    if i == 0 and dp[i][j-1] > 0 or j == 0 and dp[i-1][j] > 0 :
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# [[1,0]]
for i in range(3):
    print(i)

