class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(0,31):
            if n & 1 == 1:
                result = result | 1
            n = n >> 1
            result = result << 1
        return result



solution = Solution()
print(solution.reverseBits(43261596))