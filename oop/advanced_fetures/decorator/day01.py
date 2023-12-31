

# 函数装饰器


def my_decotor(func):
   def wrapper():
       print('befer func()')
       func()
       print('after func()')
   return wrapper


@my_decotor
def say_hello():
   print('hello world')



if __name__ == '__main__':
    say_hello()








