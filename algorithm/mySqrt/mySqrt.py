


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            result = (right + left)//2
            if result * result > x:
                right = result - 1
            elif result * result < x:
                left = result + 1
            else:
                return result
        return right

solution = Solution()
print(solution.mySqrt(8))