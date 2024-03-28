
from typing import List



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left] = nums[right]
                right -= 1
        return left

solution = Solution()
print(solution.removeElement([1,1,3,5,5],1))