from abc import ABC,abstractmethod

class Component:

    @abstractmethod
    def operator(self):
        pass

class ConcreateComponent(Component):

    def __init__(self,decorator):
        self._decorator = decorator

    def operator(self):
        return self._decorator + "ConcreateComponent"

class Decorator(ABC):
    @abstractmethod
    def operator(self,component: Component):
        pass

class ConcreateDecoratorA(Decorator):

    def operator(self,componemt: Component):
        return  f"ConcreateDecoratorA + { componemt.operator() }"

class ConcreateDecoratorB(Decorator):

    def operator(self,componemt: Component):
        return  f"ConcreateDecoratorB + { componemt.operator() }"

def client_code():
    simple = Decorator()
    component = Component()


if __name__ == '__main__':
    client_code()

