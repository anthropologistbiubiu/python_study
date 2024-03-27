from typing import List


'''
给你一个 非严格递增排列 的数组 nums ，
请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pre, cur = 0, 0
        while cur < len(nums):
            if nums[cur] == nums[pre]:
                cur += 1
            else:
                while cur - pre > 1:
                    nums[cur - 1] = nums[cur]
                    cur -= 1
                pre += 1
        return pre + 1


solution = Solution()
print(solution.removeDuplicates([1,2,2,2,3,3,4]))
print(solution.removeDuplicates([1,1,1,1,1,1,1]))
