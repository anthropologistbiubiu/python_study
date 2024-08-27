
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dfs(board,word,0,0,0)


    def dfs(self,board:List[List[str]],word:str,i:int,j :int, cur:int):
        if board[i][j] != word[cur] or i == 0:
            return
        else:
            cur+=1
        self.dfs(board,word,i-1,j,cur)
        self.dfs(board,word,i+1,j,cur)
        self.dfs(board,word,i,j-1,cur)
        self.dfs(board,word,i,j+1,cur)

