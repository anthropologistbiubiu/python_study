from typing import List



# 无重复字符串的排列组合
# https://leetcode.cn/problems/permutation-i-lcci/

# 有重复字符串的排列组合
# https://leetcode.cn/problems/permutation-ii-lcci/description/
class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        s = list(S)
        self.dfs(s, 0, ans)
        return ans
    def permutate(self, S: str) -> List[str]:
        pass
    def dfs(self,s,cur,ans :list):
        if cur == len(s):
            ans.append(''.join(s))
            return
        mset = set()
        for i in range(cur,len(s)):
            if s[i] in mset:
                continue
            mset.add(s[i])
            s[i], s[cur] = s[cur], s[i]
            self.dfs(s, cur + 1, ans)
            s[i], s[cur] = s[cur], s[i]




solution = Solution()
print(solution.permutation("ab"))