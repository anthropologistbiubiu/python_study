

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 1:
            return half * half * x
        return half * half




solution = Solution()
print(solution.myPow(2,10))