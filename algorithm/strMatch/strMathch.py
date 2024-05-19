
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass

'''

next数组的每个元素表示模式串中当前位置之前的子串的前缀和后缀的最长相等长度。
具体地，next[i]表示模式串的第0到第i-1个字符的子串中，最长的相等前缀和后缀的长度。

'''
def compute_next(pattern):
    return None

# 示例
pattern = "abababca"
next_array = compute_next(pattern)
print(f"Next array: {next_array}")
solution = Solution()
print(solution.strStr())



