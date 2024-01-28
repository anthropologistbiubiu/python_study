from abc import ABC,abstractmethod

class Handler(ABC):
    pass
class AbstractHandler():

    _next_node: Handler = None
    def handler(self,food):
        pass

    def set_next(self):
        pass


class MonkeyHandler(AbstractHandler):
    def handler(self,food):
       if food == "Banana":
            print(f"monkey eat {food}")
       else:
           super().handler()

class SquirrelHandler():
    def handler(self,food):
        if food == "Nut":
            print(f"Squireel eat {food}")
        else:
            super().next()

class DogHandler():
    def handler(self,food):
        if food == "Meatball":
            print(f"dog eat {food}")
        else:
           super().next()


def client_code():
    pass

def main():
    pass

if __name__ == '__main__':
    main()