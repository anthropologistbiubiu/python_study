from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = min(strs,key=len)
        for i in range (0,len(shortest)):
            for j in range (0,len(strs)):
                if strs[j][i] != shortest[i]:
                    return shortest[:i]
        return shortest
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 找到最短的字符串
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return shortest[:i]

        return shortest


# strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
strs = ["a","b"]
solution = Solution()
print(solution.longestCommonPrefix(strs))

