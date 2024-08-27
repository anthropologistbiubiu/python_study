
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


    def dfs(self,board:List[List[str]],word:str,i:int,j :int, cur:int):
        if board[i][j] != word[cur]:
            return