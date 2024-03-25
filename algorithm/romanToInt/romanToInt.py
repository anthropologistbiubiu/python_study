class Solution:
    """
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000
    """
'''
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

'''


def romanToInt(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
         "IV": 3, "IX": 8,
         "XL": 30, "XC": 80,
         "CD": 300, "CM": 800
         }
    result = 0
    for i, item in enumerate(s):
        if i == 0:
            result += d.get(s[0])
        else:
            result += d.get(s[i - 1:i + 1], d[item])
    return result

print(romanToInt("MCMXCIV"))