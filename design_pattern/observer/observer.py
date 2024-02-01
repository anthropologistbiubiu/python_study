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
   def notify(self):
       pass

   def attach(self):
       pass

   def detach(self):
       pass

class AbstractObserver(ABC):
    pass

class observerA:
    pass

class observerB:
    pass

