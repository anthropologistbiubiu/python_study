




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for index,item in enumerate(s):
            s_to_t[item] = t[index]
            t_to_s[t[index]] = item
        for index,item in s_to_t.items():
            if index != s_to_t.get(item) or item != t_to_s.get(index):
                return False
        return True

solution = Solution()
solution.isIsomorphic('eggp','affg')



