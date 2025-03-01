from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        result = [0]
        self.dfs(root,1,k,result)
        return result[0]

    def dfs(self, root:Optional[TreeNode],i:int,k:int, result:List[int]) -> int:
        if not root:
            return
        self.dfs(root.left,i,k,result)
        if i == k:
             result.append(root.val)
        else:
            i+=1
        self.dfs(root.right,i,k,result)
        
        
