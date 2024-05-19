from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = strs[0]
        for i in range(0,len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]
        for i in range (0,len(shortest)):
            for j in range (0,len(strs)):
                if strs[j][:i] != shortest[:i]:
                    return shortest[:i]
        return ""


strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))

