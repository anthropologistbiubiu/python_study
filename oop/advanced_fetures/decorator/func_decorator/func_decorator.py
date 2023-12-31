# 带参数的装饰器函数

def args_decorator(count):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(count):
                print(f'args_decorator {i}')
                print('befer args_decorrator')
                func(*args, **kwargs)
                print('after args_decorrator')
        return wrapper
    return decorator




@args_decorator(4)
def say_hello(*args,**kwargs):
    for item in args:
        print(item)
    for key, value in kwargs:
        print(key, value)


if __name__ == '__main__':
    say_hello(('sun','wei','ming'),{'name':'sunweiming','age':18})



