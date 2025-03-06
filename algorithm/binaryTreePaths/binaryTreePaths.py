
from typing import Optional



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return
    def dfs(self,root:Optional[TreeNode],list:List[str],path:List[int]):
        if not root:
            return
        path = path.append(path,root.val) 
        if root.left:
            self.dfs(root.left,list,path)
        if root.right:
            self.dfs(root.right,list,path)
