class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left, right = 0, 0
        maxLen = 0
        while left < right:
            if s[right] not in chars:
                right += 1
                chars.add(s[right])
                maxLen = max(maxLen,right-left+1)
            else:
                if s[left] in chars:
                    left += 1
                    chars.remove(s[left])
        return maxLen

solution = Solution()
print(solution.lengthOfLongestSubstring("abcaaaa"))
