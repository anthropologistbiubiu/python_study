
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        def dfs(start: int, total: int, comb: List[int]):
            if total == target:
                result.append(comb.copy())

            for i in range(start, len(candidates)):
                total += candidates[i]
                if total > target:
                    break
                comb.append(candidates[i])
                dfs(i, total, comb)
                total -= candidates[i]
                comb.pop()

        result = []
        comb = []
        dfs(0, 0, comb=comb)
        return result

solution = Solution()
print(solution.combinationSum([2,3,6,7],7))