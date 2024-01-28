from abc import ABC,abstractmethod
# from __future__ import annotations
from typing import Any
class Handler():
    def set_next(self):
        pass

class AbstractHandler():

    _next_node: Handler = None
    def set_next(self,handler:Handler) -> Handler:
         self._next_node = handler
         return self._next_node
    def handler(self,food):
        if self._next_node:
            self._next_node.handler(food)
        else:
            pass

class MonkeyHandler(AbstractHandler):
    def handler(self,food):
       if food == "Banana":
            print(f"monkey eat {food}")
       else:
           super().handler(food)

class SquirrelHandler(AbstractHandler):
    def handler(self,food):
        if food == "Nut":
            print(f"Squireel eat {food}")
        else:
            super().handler(food)

class DogHandler(AbstractHandler):
    def handler(self,food):
        if food == "Meatball":
            print(f"dog eat {food}")
        else:
           super().handler(food)


def client_code():
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    for food in ["Nut","Meatball","Banana"]:
        monkey.handler(food)

def main():
   client_code()

if __name__ == '__main__':
    main()