

# 函数装饰器


def my_decorator(func):
   def wrapper():
       print('befer func()')
       func()
       print('after func()')
   return wrapper

@my_decorator
def say_hello():
   print('hello world')

if __name__ == '__main__':
    say_hello()








