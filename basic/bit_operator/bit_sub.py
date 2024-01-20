



# 使用位运算实现减法
def bit_operator_sub(num1,num2):

    a = num1
    b = -num2
    c = a ^ b
    d = (a & b) << 1
    while d != 0:
        a = c
        b = d
        c = a ^ b
        d = (a & b) << 1
    return c


def main():
    print(bit_operator_sub(10,1))


if __name__ == '__main__':
    main()