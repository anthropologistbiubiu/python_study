from abc import ABC,abstractmethod

class Component:
    def operator(self):
        return "Component"

class Decorator(ABC):


    @abstractmethod
    def operator(self,component: Component):
        pass

class ConcreateDecoratorA:

    def operator(self,componemt: Component):
        return  f"ConcreateDecoratorA + { componemt.operator() }"

class ConcreateDecoratorB:
    def operator(self,componemt: Component):
        return  f"ConcreateDecoratorB + { componemt.operator() }"

def client_code():
    pass


if __name__ == '__main__':
    client_code()

