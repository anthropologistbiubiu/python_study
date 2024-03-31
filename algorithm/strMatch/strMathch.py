

from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pass


def get_next(pattern):
    next_arr = [-1] * len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j >= 0 and pattern[j + 1] != pattern[i]:
            j = next_arr[j]
        if pattern[j + 1] == pattern[i]:
            j += 1
        next_arr[i] = j
    print(next_arr)
    return next_arr

def kmp(text, pattern):
    next_arr = get_next(pattern)
    j = -1
    for i in range(len(text)):
        while j >= 0 and pattern[j + 1] != text[i]:
            j = next_arr[j]
        if pattern[j + 1] == text[i]:
            j += 1
        if j == len(pattern) - 1:
            return i - j  # 匹配成功，返回在text中的起始位置
    return -1  # 匹配失败

# 测试示例
text = "ABC ABCDAB ABCDABCDABDE"
pattern = "ABCDABD"
print(kmp(text, pattern))  # 输出：15


