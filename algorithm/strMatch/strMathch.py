
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


def compute_next(pattern):
    m = len(pattern)
    next = [-1] * m
    j = -1
    i = 0
    while i < m - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

# 示例
pattern = "abababca"
next_array = compute_next(pattern)
print(f"Pattern: {pattern}")
print(f"Next array: {next_array}")



