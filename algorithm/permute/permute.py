from typing import List


# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


'''
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums,0,ans)
        return ans
    def dfs(self,nums,cur,ans):
        if cur == len(nums)-1:
            ans.append(nums[:])
            return
        for i in range(cur, len(nums)):
            nums[i], nums[cur] = nums[cur], nums[i]
            self.dfs(nums, cur + 1,ans)
            nums[i], nums[cur] = nums[cur], nums[i]
    def sort_str(self):
        pass

solution = Solution()
print(solution.permute([1,2,3]))