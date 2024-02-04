from abc import ABC,abstractmethod

class Component:

    @abstractmethod
    def operator(self):
        pass

class ConcreateComponent(Component):

    def operator(self):
        return  " {ConcreateComponent} "

class Decorator(ABC):

    @abstractmethod
    def operator(self):
        pass

class ConcreateDecoratorA(Decorator):

    def __init__(self,component):
        self._component = component
    def operator(self):
        return  "Decorated By ConcreateDecoratorA" + self._component.operator()

class ConcreateDecoratorB(Decorator):

    def __init__(self,component):
        self._component = component
    def operator(self,componemt: Component):
        return  "Decorated By ConcreateDecoratorB"  + self._component.operator()

def client_code():
    component = ConcreateComponent()
    decorator1 = ConcreateDecoratorA(component )
    print(decorator1.operator())


if __name__ == '__main__':
    client_code()

