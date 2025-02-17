


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        max_repeat = 0
        for i in range(n):
            j = i
            repeat = 0
            while  i + m < n and sequence[i:i+n] == word:
                repeat += 1
                i += m
                max_repeat = max(repeat,max_repeat)
        return max_repeat




