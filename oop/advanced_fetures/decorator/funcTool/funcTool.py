
from functools import wraps



def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('befor decorator')
        func(*args,**kwargs)
        print('aftr decorator')
    return wrapper


@my_decorator
def say_hello():
   print('say_hello')
if __name__ == '__main__':
    say_hello()