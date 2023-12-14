


# 这里参考c++ 写二叉树的过程来写好二叉树的数据结构


class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,key):
        self.root = self._insert(self.root,key)
    def _insert(self,root,key):
        if root is None:
            root = Node(key)
        elif root.data > key:
           root.left = self._insert(root.left,key)
        elif root.data < key:
            root.right = self._insert(root.right,key)
        return root
    def preorder_traversal(self):
        if self.root is None:
            print(None)
        self._preorder_traversal(self.root)
    def _preorder_traversal(self,root):
        if root is None:
            return
        print(root.data)
        self._preorder_traversal(root.left)
        self._preorder_traversal(root.right)
    def update(self):
        pass
    def delete(self):
        pass

mytree = BinaryTree()
mytree.insert(1)
mytree.insert(2)
mytree.insert(3)
mytree.preorder_traversal()
