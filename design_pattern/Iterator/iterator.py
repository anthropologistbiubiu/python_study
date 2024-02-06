from abc  import abstractmethod

class Collection:
    pass

class Iterator():

   _reverse = False
   def __init__(self,collection):
       self.collection = collection

   def __iter__(self):
      pass

   def get_reverse_iterator(self):
       pass

def client_code():
    pass

if __name__ == '__main__':
    client_code()

