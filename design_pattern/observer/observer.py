from abc import ABC, abstractmethod



class AbstractSubject:
    pass

class Subject(ABC):

   @abstractmethod
   def notify(self):
        pass

   @abstractmethod
   def attach(self):
       pass

   @abstractmethod
   def detach(self):
       pass




class AbstractObserver:
    pass

class observerA:
    pass

class observerB:
    pass

