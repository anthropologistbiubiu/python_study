from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for index, num in enumerate(nums):
            if index > max_reachable:
                return False
            max_reachable = num + index if num + index > max_reachable else max_reachable
            if max_reachable >= len(nums) -1:
                return True
        return False


nums = [2, 3, 1, 1, 4]
solution = Solution()
print(solution.canJump(nums))
