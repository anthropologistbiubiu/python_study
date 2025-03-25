from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = len(nums) + 1
        compare = 0
        for right in range(0,len(nums)):
            compare += nums[right] 
            while left <= right:
                if compare >= target:
                    min_length = min(right - left + 1,min_length) 
                    compare -= nums[left]
                    left += 1
                else:
                    break
        if min_length > len(nums):
            return 0
        return min_length
