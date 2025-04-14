
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum = float('inf')
        for index,num in enumerate(nums):
            left = index + 1 
            right = len(nums) - 1 
            while left < right:
                current_sum = nums[left] + nums[right] + num
                if abs(current_sum - target) < abs (closest_sum -target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum
            
                
             



solution = Solution()

print(solution.threeSumClosest([1,2,3,4],5))
            
    
