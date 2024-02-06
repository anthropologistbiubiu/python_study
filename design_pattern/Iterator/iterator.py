from abc  import abstractmethod

class Collection:
    pass

class Iterator():

   _pos = 0
   def __init__(self,collection,reverse):
       self.collection = collection
       self._reverse = reverse

   def __iter__(self):
       try:
        if self._reverse:
            value = self.collection[self._pos]
            self._pos += 1
            return value
       except StopIteration as e:
           raise e
   def get_reverse_iterator(self):
       pass

def client_code():
    pass

if __name__ == '__main__':
    client_code()

