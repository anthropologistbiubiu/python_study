class Solution:
    def compute_next(self,pattern) -> [int]:
        i = 0
        j = -1
        next = [-1] * len(pattern)
        while i < len(pattern) - 1:
            if j == -1 or pattern[i] == pattern[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next

    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        next_array = self.compute_next(needle)
        while i < n and j < m:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]
        if j == m:
            return i - j
        else:
            return -1




'''
next数组的每个元素表示模式串中当前位置之前的子串的前缀和后缀的最长相等长度。
具体地，next[i]表示模式串的第0到第i-1个字符的子串中，最长的相等前缀和后缀的长度。
'''

# 示例
pattern = "ABABCABAB"
text = "ABABDABACDABABCABAB"
solution = Solution()
print(solution.compute_next(pattern))
print(solution.strStr(text,pattern))



