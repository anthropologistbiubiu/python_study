from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        if len(nums) == 3 and nums[0] + nums[1] + nums[2] == 0:
             ans.append([nums[0],nums[1],nums[2]])
        for i in range(0,len(nums)-3):
            left = i + 1
            right = len(nums) -1
            while left < right:
                if nums[i] > 0:
                    break
                if nums[i] == nums[i-1] and i > 0:
                    break
                if nums[i] + nums[left] + nums[right] == 0:
                    print(i,nums[i])
                    ans.append([nums[i], nums[left], nums[right]])
                    left_value = nums[left]
                    right_value = nums[right]
                    # -4, -1, -1, 0, 1, 2))
                    while left < right and left_value == nums[left]:
                        left += 1
                    while left < right and right_value == nums[right]:
                        right -= 1
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

# print(solution.threeSum([0,0,0]))
# print(solution.threeSum([0,1,1]))
# print(solution.threeSum([0,0]))

'''
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
'''
