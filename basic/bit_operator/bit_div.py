# 180 /25 向下整除

def division(a,b):
    ans = 0
    for i in range(64, 1, -1):
        if b * (2 << i) < a:
            a = a - b * (2 << i)
            ans += 2 << i
    return ans


def main():
   print(division(100,25))

if __name__ == '__main__':
    main()