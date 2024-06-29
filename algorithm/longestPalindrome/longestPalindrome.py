

# 最长回文字串
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s
        dp = [[0]*(len(s)+1)]*(len(s)+1)
        for i in range(0,len(s)):
            dp[i][i] = True
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
            else:
                dp[i][i+1] = False
        for i in range(3,len(s)-1):
            pass


solution = Solution()
solution.longestPalindrome("SSSS")
