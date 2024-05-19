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


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    next = compute_next(pattern)
    i = 0
    j = 0

    while i < n:
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]

        if j == m:
            print(i)
            print(f"Pattern found at index {i - j}")
            # j = next[j - 1]  # Continue searching for other occurrences


# 示例
pattern = "ABABCABAB"
next_array = compute_next(pattern)
print(f"Pattern: {pattern}")
print(f"Next array: {next_array}")

text = "ABABDABACDABABCABAB"
kmp_search(text, pattern)
