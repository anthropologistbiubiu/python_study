

# 使用并查集的解法
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        length = len(s)
        map = {}
        difference = 0
        for i in range (0,length):
            map[s[i]] = i
        for i in range (0,length):
            difference += abs(map.get(t[i]) - i)
        return difference




solution = Solution()
#s = "abcde", t = "edbac"
print(solution.findPermutationDifference('abcde','edbac'))



