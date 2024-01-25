from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass

# 定义一个普通的类，没有显式继承 Handler 类，也没有实现 handle 方法
class CustomClass(Handler):
    pass

def some_function(handler: Handler):
    result = handler.handle("Example Request")
    print(result)

custom_object = CustomClass()

try:
    some_function(custom_object)
except TypeError as e:
    print(f"TypeError: {e}")
