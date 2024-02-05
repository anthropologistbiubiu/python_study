from abc import ABC,abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):

    def request(self):
        print('send real request')

class Proxy(Subject):
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
        print(f'logging the cost of request')

def client_code(subject:Subject):
    subject.request()

if __name__ == '__main__':
    request = RealSubject()
    proxy = Proxy(request)
    client_code(proxy)

