
def iter_decorator(func):
    def wrapper(*args,**kwargs):
        try:
            print('befor iter_decorator')
            result =  func(*args,**kwargs)
            print('afetr iter_decorator')
            return result**2
        except StopIteration as e:
             print(f'iter_decorator fail  {e}')
             raise e
        else:
            print('iter success')
    return wrapper

class MyIterObject:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    @iter_decorator
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


# 加一个装饰器函数进去，对迭代失败的边界条件进行修饰,采用try expect 方式对这个过程进行判别


def test_iter():
        my_object = MyIterObject([1,2,3,4,5])
        for item in my_object:
            print(item)

def test_iter_fail():
        my_object = MyIterObject([1,2,3,4,5])
        for item in my_object:
            print(item)

if __name__ == '__main__':
    test_iter()


