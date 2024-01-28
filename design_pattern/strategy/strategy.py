from abc import abstractmethod

class Context:
    def __init__(self,strategy):
        self._strategy = strategy
    def do_logic(self):
        self._strategy.do_logic()
    @property
    def strategy(self):
        pass

    @strategy.setter
    def set_strategy(self,strategy):
        pass

class Strategy:
    @abstractmethod
    def do_logic(self):
        pass

class concrecteStrategyA(Strategy):
    def do_logic(self):
        print("concrecteStrategyA")




class concrecteStrategyB(Strategy):
    pass


def client_code():
  strategyA = concrecteStrategyA()
  context = Context(strategyA)
  context.do_logic()
  print()
  strategyB = concrecteStrategyB()
  context = Context(strategyB)
  context.do_logic()

def main():
   client_code()

if __name__ == '__main__':
   main()