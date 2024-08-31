from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        longest, jumps, end = 0, 0, 0
        if len(nums) == 1:
            return 0
        for index, num in enumerate(nums):
            longest = max(longest, num + index)
            if index == end:
                jumps += 1
                end = longest
                if end >= len(nums) - 1:
                    break
        return jumps




nums = [2,3,1,1,4]
#2
solution = Solution()
print(solution.jump(nums))


nums = [2,3,0,1,4]
print(solution.jump(nums))
#输出: 2
nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
print(solution.jump(nums))
