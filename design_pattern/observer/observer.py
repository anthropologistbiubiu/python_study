from abc import ABC, abstractmethod


class AbstractSubject:
    pass

class Subject(ABC):

   @abstractmethod
   def update(self):
        pass

class AbstractObserver:
    pass

class observerA:
    pass

class observerB:
    pass

