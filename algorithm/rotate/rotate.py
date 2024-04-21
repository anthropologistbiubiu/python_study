import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(0,n-i):
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]
        print(matrix)
        for i in range(0,math.floor(n/2)):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution = Solution()
solution.rotate(matrix)
print(matrix)