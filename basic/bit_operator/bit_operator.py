


# 位运算符表示➕➖✖️➗

def bit_operator_add(a, b):
    c = a ^ b
    d = (a & b) << 1
    while d != 0:
        a = c
        b = d
        c = a ^ b
        d = (a & b) << 1
    return c


def main():
    print(bit_operator_add(1000,1))
if __name__ == '__main__':
  main()

