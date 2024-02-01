import random
from abc import ABC, abstractmethod


class AbstractSubject(ABC):

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass


class Subject(AbstractSubject):

    _observers = []
    _status = 0
    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def attach(self,observer):
        self._observers.append(observer)

    def detach(self):
        self._observers.remove()

    def do_some_logic(self):
        print("\nSubject: I'm doing something important.")
        self._status = random.randint(1,10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class AbstractObserver(ABC):
    pass

class observerA:
    pass

class observerB:
    pass

