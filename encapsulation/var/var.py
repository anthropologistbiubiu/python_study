


class MyClass:
    def __init__(self):
        self.__private_variable = 10

    def __private_method(self):
       print('__private_method')


def main():
   obj = MyClass()
   print(obj.__pirvate_variable)
   obj.__private_method()

if __name__ == '__main__':
    main()