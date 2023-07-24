
import sys
sys.path.append("./mymodule")

import mymodule
def main():
   try:
        ans = mymodule.Add(3,5)
        print(ans)
        hello = mymodule.greet("sunweiming")
        print(hello)
   except Exception as e:
       print("Exception ",e)

if __name__ == '__main__':
    main()