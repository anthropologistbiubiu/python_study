
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        even_length = 0
        odd_length = 0
        is_odd  = False

        for item in s:
            if item not in m:
                m[item] = 1
            else:
                m[item] = m[item] + 1

        for value in m.values():
            if value % 2 == 0:
                even_length += value
            else:
                odd_length += (value -1)
                is_odd = True
        if is_odd:
            return even_length + odd_length + 1 
        return even_length 