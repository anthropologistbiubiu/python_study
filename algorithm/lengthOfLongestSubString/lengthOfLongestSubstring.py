class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left, right = 0, 0
        maxLen = 0
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                maxLen = max(maxLen,right-left+1)
                right += 1
            else:
                if s[left] in chars:
                    chars.remove(s[left])
                    left += 1
        return maxLen

