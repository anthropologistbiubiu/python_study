


def iter_decorator(func):
    def wrapper(*args,**kwargs):
        print('iter_decorator')
        result =  func(*args,**kwargs)
        print('iter_decorator')
        return result
    return wrapper

class MyIterObject:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    @iter_decorator
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# 加一个装饰器函数进去，对迭代失败的边界条件进行修饰,采用try expect 方式对这个过程进行判别


def test_iter():
    try:
        my_object = MyIterObject([1,2,3,4,5])
        for item in my_object:
            print(item)
    except MyIterObject as e:
        print(f'MyIterObject  {e}')
    else:
        print('iter success')

def test_iter_fail():
    try:
        my_object = MyIterObject([1,2,3,4,5])
        for item in my_object:
            print(item)
    except MyIterObject as e:
        print(f'MyIterObject  {e}')
    else:
        print('iter success')

if __name__ == '__main__':
    test_iter()


