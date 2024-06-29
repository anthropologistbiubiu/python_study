class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set = set()
        left, right = 0, 0
        maxLen = 0
        while left < right:
            if s[right] not in set:
                right += 1
                set.add(s[right])
            else:
                if s[left] in set:
                    left += 1
        return maxLen

solution = Solution()
print(solution.lengthOfLongestSubstring("abcaaaa"))
