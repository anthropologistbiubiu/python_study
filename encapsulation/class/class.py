


class MyClass:

    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

def main():
    obj = MyClass('zhangsan')
    print(obj.get_name())


if __name__ == '__main__':
    main()