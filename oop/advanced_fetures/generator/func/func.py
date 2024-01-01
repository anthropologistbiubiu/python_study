


# 生成器表达式

gen1 = (x for x in range (5))

try:
    while True:
        item = next(gen1)
        print(item)
except StopIteration as e :
    print('StopIteration ',e)

# 生成器函数

def my_generator():
    yield 1
    yield 2
    yield 'sunweiming'


gen2 = my_generator()
for item in gen2:
    print('gen2',item)


# 迭代生成器



