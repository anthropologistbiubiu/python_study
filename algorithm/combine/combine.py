from typing import List

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []

        def dfs(start: int, comb: List[int]):
            if len(comb) == k:
                result.append(comb.copy())
            for i in range(start, n + 1):
                comb.append(i)
                dfs(start=i + 1, comb=comb)
                comb.pop()
        dfs(1, comb)
        return result

solution = Solution()
print(solution.combine(n=5,k=3))