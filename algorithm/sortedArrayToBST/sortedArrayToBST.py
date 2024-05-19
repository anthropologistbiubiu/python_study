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
        middle_index = len(nums) // 2
        value = nums[middle_index]
        node = TreeNode(value,None,None)
        node.left = self.sortedArrayToBST(nums[:middle_index])
        node.right = self.sortedArrayToBST(nums[middle_index+1:])
    def sortedArrayToBSTPrint(self):
        pass

solution = Solution()
solution.sortedArrayToBST([1,2,3,4,5,6])
solution.sortedArrayToBSTPrint()
