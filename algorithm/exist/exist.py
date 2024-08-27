
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs(board,word,0,0,0)

    def dfs(self, board: List[List[str]], word: str, i: int, j: int, cur: int) -> bool:
        if cur == len(word):
            return True
        if i < 0 or j < 0 or j == len(board[0]) or i == len(board):
            return False
        if board[i][j] != word[cur]:
            pass
        else:
            cur += 1
        return self.dfs(board, word, i - 1, j, cur) or self.dfs(board, word, i + 1, j, cur) or self.dfs(board, word, i, j - 1, cur) or self.dfs(board, word, i, j + 1, cur)


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
solution = Solution()
print(solution.exist(board, word))
