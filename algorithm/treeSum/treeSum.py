from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-3):
            left = i + 1
            right = len(nums) -1
            while left < right:
                if nums[i] > 0:
                    break
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    break
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        return ans
'''
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
'''

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,0,0]))
print(solution.threeSum([0,1,1]))
print(solution.threeSum([0,0]))

'''
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
'''
