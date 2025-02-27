



class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        self.dfs(root,targetSum=targetSum)
        return path
    def dfs(self, root: Optional[TreeNode], targetSum: int):
        if root is None:
            return 
        if root.left not None:
            self.pathSum(root.left,targetSum=targetSum-root.value)
