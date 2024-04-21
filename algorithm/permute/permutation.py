from typing import List



# 无重复字符串的排列组合
# https://leetcode.cn/problems/permutation-i-lcci/

# 有重复字符串的排列组合
# https://leetcode.cn/problems/permutation-ii-lcci/description/


# 全排列
# https://leetcode.cn/problems/VvJkup/
# 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。



class Solution:

    def permutation1(self, S: str) -> List[str]:
        ans = []
        s = list(S)
        self.dfs1(s, 0, ans)
        return ans
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        ans_list = []
        for i in range(len(nums)):
            nums1 = nums[:i] + nums[i + 1:]
            ans = self.permute(nums1)
            for an in ans:
                ans_list.append(nums[i:i+1]+ an)
        return ans_list
    def permutePlus(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        ans_list = []
        for i in range(len(nums)):
            for an in self.permute(nums[:i] + nums[i + 1:]):
                ans_list.append(nums[i:i+1]+ an)
        return ans_list

    def dfs1(self,s,cur,ans :list):
        if cur == len(s):
            ans.append(''.join(s))
            return
        mset = set()
        for i in range(cur,len(s)):
            if s[i] in mset:
                continue
            mset.add(s[i])
            s[i], s[cur] = s[cur], s[i]
            self.dfs1(s, cur + 1, ans)
            s[i], s[cur] = s[cur], s[i]
    def dfs2(self,s:list,cur:int,ans:list):
        if cur == len(s)-1:
            ans.append(''.join(s))
            return
        for i in range(cur,len(s)):
            s[cur],s[i] = s[i],s[cur]
            self.dfs2(s,cur+1,ans)
            s[cur],s[i] = s[i],s[cur]


solution = Solution()
print(solution.permutation1("ab"))
print(solution.permute([1,2,3]))