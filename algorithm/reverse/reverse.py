




class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        result = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        while y != 0:
            pop = y % 10
            y = y // 10
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
                return 0
            if result < INT_MIN // 10 or (result == INT_MIN // 10 and pop < -8):
                return 0
            result = result * 10 + pop
        if x < 0:
            return -result
        return result



solution = Solution()
print(solution.reverse(-321))
