# 最长回文字串
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]
        # dp = [[False] * (len(s))] * (len(s))
        maxLen = 0
        st = 0
        for i in range(0, len(s)):
            dp[i][i] = True
            st = i
            maxLen = 1
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                st = i
                maxLen = 2
            else:
                dp[i][i + 1] = False
        for length in range(3, len(s)+1):
            for i in range(0, len(s) - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    st = i
                    maxLen = length
                else:
                    dp[i][j] = False
        '''
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if dp[i][j] and j-i > maxLen:
                    maxLen = j-i + 1
                    ans = s[i:j+1]
                    print(i,j)
        '''
        return s[st:st+maxLen]


solution = Solution()
print(solution.longestPalindrome("cbba"))
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("ccc"))
print(solution.longestPalindrome("ccd"))
