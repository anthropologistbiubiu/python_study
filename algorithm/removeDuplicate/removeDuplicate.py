from typing import List


'''
给你一个 非严格递增排列 的数组 nums ，
请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        pre, cur = 0, 0
        for i,num in enumerate(nums):
            if nums[cur] == nums[pre]:
                cur+=1
            elif cur-pre ==1:
                continue
            else:
               nums[cur-1] == cur[cur]
                ## nums[cur]
        return nums.count()
