from typing import List

class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        print(ans)
        for i in range(numRows):
            rows = [0] * (i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    rows[j] = 1
                else:
                    rows[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(rows)
        return ans



class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            rows = [0] * (i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    rows[j] = 1
                else:
                    rows[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(rows)
        return ans[rowIndex]



solution = Solution2()
print(solution.getRow(3))

