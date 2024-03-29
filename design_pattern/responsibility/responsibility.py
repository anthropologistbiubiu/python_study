from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional



class AbstractHandler():

    _next_handler = None
    def set_next(self, handler):
        self._next_handler = handler
        return handler
    # @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):

    _next_handler = None
    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return f"No one can eat the {request}"

class SquirrelHandler(AbstractHandler):
    _next_handler = None
    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return f"No one can eat the {request}"


class DogHandler(AbstractHandler):

    _next_handler = None
    def set_next(self, handler):
        self._next_handler = handler
        return self._next_handler

    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return f"No one can eat the {request}"


def client_code(handler) -> None:

    for food in ["Nut", "Banana", "Pear","Meat"]:
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    print("Chain: Monkey > Squirrel > Dog")
    monkey.set_next(squirrel).set_next(dog)
    client_code(monkey)
    print("\n")
    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
    print("\n")