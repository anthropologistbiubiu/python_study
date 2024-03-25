class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"":""}
        result = 0
        for i, item in enumerate(s):
            if i == 0:
               result += d.get(s[0])
        else:
            result += d.get(s[i-1:i+1],d[item])
        return result



solution = Solution()
print(solution.romanToInt("IV"))