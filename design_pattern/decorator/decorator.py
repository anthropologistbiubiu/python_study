from abc import ABC,abstractmethod

class Component:
    pass

class Decorator(ABC):

    @abstractmethod
    def operator(self):
        pass

class ConcreateDecoratorA:

    def operator(self):
        pass

class ConcreateDecoratorB:
    def operator(self):
        pass


def client_code():
    pass


if __name__ == '__main__':
    client_code()

