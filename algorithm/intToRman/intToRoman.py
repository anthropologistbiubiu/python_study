

class Solution:
    def intToRoman_my(self, num: int) -> str:
        romanPairs = [
            {1000: "M"}, {900: "CM"}, {500: "D"}, {400: "CD"},
            {100: "C"}, {90: "XC"}, {50: "L"}, {40: "XL"},
            {10: "X"}, {9: "IX"}, {5: "V"}, {4: "IV"}, {1: "I"}
        ]
        resultRoman = ""
        while num > 0:
            for pair in romanPairs:
                for key, item in pair.items():
                    count = num // key
                    if count > 0:
                        resultRoman += item * count
                        num = num - key * count
                    else:
                        continue
        return resultRoman
    def intToRoman(self, num: int) -> str:
        romanPairs = {1000: "M", 900: "CM", 500: "D", 400: "CD",100: "C"
            , 90: "XC", 50: "L", 40: "XL",10: "X",
        9: "IX", 5: "V", 4: "IV", 1: "I"}
        resultRoman = ""
        for key,value in romanPairs.items():
            while num >= key:
                resultRoman += value
                num -= key
        return resultRoman





solution = Solution()
# 1994 的罗马数字形式是 "MCMXCIV"。
print(solution.intToRoman(1994))