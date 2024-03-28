
from typing import List



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                nums[left] = nums[right]


solution = Solution()
print(solution.removeElement([1,2,3,4,5],5))