



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for item in s[::-1]:
            if item == " ":
                break
            count += 1
            print(item)
        return count


solution = Solution()
print(solution.lengthOfLastWord("hello world"))



