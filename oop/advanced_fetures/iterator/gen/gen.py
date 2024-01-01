


# 使用生成器表达式来迭代


def gen_func(data):
    for item in data:
        yield item

def iter_generator(data):
    gen = gen_func(data)
    for item in gen:
        print(item)

if __name__ == '__main__':
   iter_generator([1,2,3,4,5])
