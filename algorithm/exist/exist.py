
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int, cur: int) -> bool:
        if cur == len(word):
            return True
        if i < 0 or j < 0 or j == len(board[0]) or i == len(board):
            return False
        tem = board[i][j]
        if board[i][j] == word[cur]:
            board[i][j] = '#'
            cur += 1
        else:
            return False
        found = (self.dfs(board, word, i - 1, j, cur) or
                 self.dfs(board, word, i + 1, j, cur) or
                 self.dfs(board, word, i, j - 1, cur) or
                 self.dfs(board, word, i, j + 1, cur))
        board[i][j] = tem
        return found


#board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
#word = "ABCCED"
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
solution = Solution()
print(solution.exist(board, word))
