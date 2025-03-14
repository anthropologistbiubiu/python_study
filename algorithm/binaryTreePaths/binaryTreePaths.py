
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
        return pathSum

    def dfs(self,root:Optional[TreeNode],pathSum:List[str],path:List[int]):
        if not root:
            return
        path.append(root.val) 
        if not root.left and not root.right:
            result = "->".join(map(str,path[:]))
            pathSum.append(result)
            path.pop()
            return
        self.dfs(root.left,pathSum,path)
        self.dfs(root.right,pathSum,path)
        path.pop()
