

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
               node = node.children[char]
            else:
                node.children[char] = Node()
                node = node.children[char]
        node.is_End_word = True



def main():
    pass

if __name__ == '__main__':
    main()






