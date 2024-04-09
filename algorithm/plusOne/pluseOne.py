from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1,-1,-1):
            print(i)
            if digits[i] != 9:
                digits[i] +=1
                return digits
            else:
                digits[i] = 0
            if i == 0:
                digits.append(0)
                digits[0] = 1
        return digits


solution = Solution()
print(solution.plusOne([9,8,9]))