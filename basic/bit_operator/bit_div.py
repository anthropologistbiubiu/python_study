# 180 /25 向下整除

def division(a,b):
    ans = 0
    for i in range(64, -1, -1):
        if a - b * (1 << i) >= 0:
            a = a - b * (1 << i)
            ans += (1 << i)
    return ans


def main():
   print(division(100,34))

if __name__ == '__main__':
    main()