from abc import ABC,abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_logic(self):
        pass
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    def do_logic(self):
        self._strategy.do_logic()
    @property
    def strategy(self):
        pass
    @strategy.setter
    def set_strategy(self,strategy):
        pass


class concrecteStrategyA(Strategy):
    def do_logic(self):
        print("concrecteStrategyA")

class concrecteStrategyB(Strategy):
    def do_logic(self):
        print("concrecteStrategyB")


def client_code():
  strategyB = concrecteStrategyB()
  context = Context(strategyB)
  context.do_logic()

def main():
   client_code()

if __name__ == '__main__':
   main()