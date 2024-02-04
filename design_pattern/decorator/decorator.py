from abc import ABC,abstractmethod

class Component:
    def operator(self):
        return "Component"

class ConcreateComponent(Component):

    def operator(self):
        pass

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

