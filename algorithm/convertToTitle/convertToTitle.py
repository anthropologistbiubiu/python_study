

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            a = columnNumber // 26
            b = columnNumber % 26
            columnNumber = a
            c = str(b)
            result = result + c
        return result








print(28//26)
print(28 % 26)

