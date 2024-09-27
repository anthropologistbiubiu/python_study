from typing import List




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        low ,high = 0, rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            mid_value = matrix[mid // cols][mid % cols]
            if target == mid_value:
                return True
            elif target < mid_value:
                high = mid - 1
            else:
                low = mid + 1
        return False