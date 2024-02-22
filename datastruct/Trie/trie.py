

class Node:
    def __init__(self):
        self.children = {}
        self.is_End_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    def Insert(self,word):
        node = self.root
        for  char in word:
            if char in node.children:
                pass












