from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

       if root.left and root.right:
            return root.left.val == root.right.val
       else:
            pass