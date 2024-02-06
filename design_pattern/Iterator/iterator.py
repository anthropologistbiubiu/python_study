from abc  import abstractmethod
from collections.abc import  Iterator,Iterable

class WordIterator(Iterator):

   _pos = 0
   def __init__(self,collection,reverse):
       self.collection = collection
       self._reverse = reverse

   def __next__(self):
       try:
            value = self.collection[self._pos]
            if self._reverse:
                self._pos += 1
            else:
                self._pos -= 1
            return value
       except  IndexError:
           raise StopIteration()


class WordCollection(Iterable):

    def __init__(self):
        self.datas = []

    def add(self,item):
        self.datas.append(item)

    def __getitem__(self, index):
        return self.datas[index]

    def __iter__(self):
        return WordIterator(self,True)

    def get_reverse_iterator(self):
        return WordIterator(self,False)
def client_code():
    datas = WordCollection()
    datas.add("first")
    datas.add("second")
    datas.add("third")
    print("\n".join(datas))

    print("\n".join(datas.get_reverse_iterator()))


if __name__ == '__main__':
    client_code()

