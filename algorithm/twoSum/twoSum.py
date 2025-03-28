


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,value in enumerate(numbers):
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right)  // 2
                if numbers[mid] > target - value:
                    right = mid -1
                elif numbers[mid] < target -value:
                    left = mid + 1
                else:
                    return [i+1,mid+1]
        return []

solution = Solution()
print(solution.twoSum([1,2,3,4],3))
