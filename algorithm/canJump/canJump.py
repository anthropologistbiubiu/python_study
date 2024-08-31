from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range (0,len(nums))]
        dp[0] = nums[0]
        for num in nums:
            print(num)




nums = [2, 3, 1, 1, 4]

solution = Solution()
solution.canJump(nums)
