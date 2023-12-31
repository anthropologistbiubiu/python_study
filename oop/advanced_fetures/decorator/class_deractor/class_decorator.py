



class MyDecorator:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('befor somethings happens')
        self.func(*args,**kwargs)
        print('after somethings happens')

@MyDecorator
def say_hello():
    print('hello world')

if __name__ == '__main__':
    say_hello()