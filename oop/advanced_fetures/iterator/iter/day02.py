

# 对于支持可迭代协议的数据对象可以采用内置函数,iter 和next 来迭代

my_iter = iter([1,2,3,4,5])

try:
    while True:
        item = next(my_iter)
        print('item:',item)
except StopIteration as e:
        print(f'StopIteration {e}')
