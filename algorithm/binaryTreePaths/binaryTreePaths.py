
from typing import Optional



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        pathSum = []
        path = []
        self.dfs(root,pathSum,path)
        return list

    def dfs(self,root:Optional[TreeNode],pathSum:List[str],path:List[int]):
        if not root:
            result = "->".join(map(str,path[:]))
            pathSum.append(result)
            path = path.pop()
            return
        path.append(root.val) 
        if root.left:
            self.dfs(root.left,pathSum,path)
        if root.right:
            self.dfs(root.right,pathSum,path)
