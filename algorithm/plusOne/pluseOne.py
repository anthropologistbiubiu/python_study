from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1,-1,-1):
            if i != 9:
                digits[i] +=1
                return digits
            else:
                for j in range (i,len(digits),1):
                    digits[j] = 0

        return digits


solution = Solution()
print(solution.plusOne([1,2,9]))