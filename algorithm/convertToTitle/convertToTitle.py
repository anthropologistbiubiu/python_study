

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        map = {
            0:"Z",1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
            10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
            19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }
        while columnNumber > 0:
            a = columnNumber // 26
            b = columnNumber % 26
            if columnNumber == 26:
                result = 'Z' + result
                break
            columnNumber = a
            # print(a,b)
            c = map.get(b)
            result = c + result
        return result


solution = Solution()
print(solution.convertToTitle(28))
print(solution.convertToTitle(52))
print(solution.convertToTitle(1))
print(solution.convertToTitle(26))
print(solution.convertToTitle(26*26))
print(solution.convertToTitle(701))
print(solution.convertToTitle(2147483647))



#输出："FXSHRXW"








