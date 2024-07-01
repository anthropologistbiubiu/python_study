




class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        pop = 0
        while x != 0:
            pop = x % 10
            x = x // 10
            result = result * 10 + pop
        return result



solution = Solution()
print(solution.reverse(321))
