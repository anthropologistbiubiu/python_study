




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return True
        s_to_t = {}
        t_to_s = {}
        for index in range (0,len(s)):
            char_s = s[index]
            char_t = t[index]
            if char_s in s_to_t:
                if char_t != s_to_t.get(char_s):
                    return False
            else:
                s_to_t[char_s] = char_t
            if char_t in t_to_s:
                if char_s != t_to_s.get(char_t):
                    return False
            else:
                t_to_s[char_t] = char_s
        return True

solution = Solution()
print(solution.isIsomorphic('egg', 'aff'))
# print(solution.isIsomorphic('foo','bar'))
