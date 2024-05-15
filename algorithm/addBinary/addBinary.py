


class Solution:
        def addBinary(self, a: str, b: str) -> str:
            result = ''
            carry = 0
            index = 0
            a = a[::-1]
            b = b[::-1]
            while index < len(a) and index < len(b):
                result = str((carry + int(a[index]) + int(b[index])) % 2) + result
                carry = (carry + int(a[index]) + int(b[index])) // 2
                index += 1
            while index < len(a):
                result = str((carry + int(a[index])) % 2) + result
                carry = (carry + int(a[index])) // 2
                index += 1
            while index < len(b):
                result = str((carry + int(b[index])) % 2) + result
                carry = (carry + int(b[index])) // 2
                index += 1
            if carry == 1:
                result = str(carry) + result
            return result


