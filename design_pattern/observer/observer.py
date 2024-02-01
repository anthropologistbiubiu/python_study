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
        print(f"Subject: My state has just changed to: {self._status }")
        self.notify()



class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class observerA(AbstractObserver):
   def update(self,subject: Subject):
       if subject._status > 3:
           print(f'observerA { subject._status }')

class observerB(AbstractObserver):
    def update(self,subject :Subject):
        if subject._status > 3:
            print(f'observerB {subject._status}')

def client_code():
    observer1 = observerA()
    observer2 = observerB()
    subject = Subject()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.do_some_logic()




def main():
   client_code()

if __name__ == '__main__':
    main()