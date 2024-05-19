from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        value = nums[len(nums)] // 2
        node = TreeNode(value,None,None)
        value.left = self.sortedArrayToBST(nums)
        value.right = self.sortedArrayToBST(nums)

solution = Solution()
solution.sortedArrayToBST([1,2,3,4,5,6])
