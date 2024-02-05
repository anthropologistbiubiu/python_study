from abc import ABC,abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):

    def request(self):
        print('end real request')

class proxy():
    def __init__(self, subject: RealSubject):
        self.subject = subject

    def request(self):
        if self.access_status():
            self.subject.request()
        self.log_access()

    def access_status(self) -> bool:
        print(f"get access_status")
        return True
    def log_access(self):
        print(f'logging the cost of request',end='')

def client_code(subjectV):
    pass

if __name__ == '__main__':
    client_code()

