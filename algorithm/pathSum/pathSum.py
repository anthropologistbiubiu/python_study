
from typing import Optional
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return  []
        path = []
        numbers = []
        self.dfs(root,targetSum,path,numbers)
        return path

    def dfs(self, root: Optional[TreeNode], targetSum: int,path: List[List[int]],numbers:List[int]):

        if root.left is None and root.right is None:
            if targetSum == root.val:
                numbers.append(root.val)
                path.append(numbers[:])
                numbers.pop()
            return
        numbers.append(root.val)
        if not root.left:
            self.dfs(root.left,targetSum-root.val,path,numbers)
        if not root.right :
            self.dfs(root.right,targetSum-root.val,path,numbers)
        numbers.pop()
