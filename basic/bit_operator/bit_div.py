# 180 /25 向下整除

def division(a,b):
    ans = 0
    for i in range(64, 0, -1):
        if a - b * (2 << i) >= 0:
            a = a - b * (2 << i)
            ans += (2 << i)
    return ans


def main():
   print(division(100,2))

if __name__ == '__main__':
    main()