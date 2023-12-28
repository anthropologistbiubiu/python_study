import sys
sys.path.append('/Users/biubiu/Documents/python_study/basic/')

from ..my_math import my_math

if __name__ == '__main__':
    tool = my_math.mathTool()
    print(tool.sum([x for x in range(101)]))
    print(tool.sub(1,2))