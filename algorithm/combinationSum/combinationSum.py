
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        def dfs(i: int, total: int, comb: List[int]):
            if total + candidates[i] == target:
                result.append(comb.copy())
