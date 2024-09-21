




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for index,item in enumerate(s):
            s_to_t[item] = t[index]
            t_to_s[t[index]] = item

