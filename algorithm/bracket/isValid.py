
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"{": "}", "(": ")", "[": "]"}
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if i != dic[left]:
                    return False
        if len(stack) > 0:
            return False
        return True



solution = Solution()

print(solution.isValid("]"))

