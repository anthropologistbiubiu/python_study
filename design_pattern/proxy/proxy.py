from abc import ABC,abstractmethod


class Subject(ABC):

    @abstractmethod
    def operator(self):
        pass

class RealSubject(Subject):
    def operator(self):
        pass


class proxy:
    pass









