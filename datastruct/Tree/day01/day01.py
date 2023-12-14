


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
            root = None(key)
        elif root.data > key:
           root.left = self._insert(root.left,key)
        else:
            root.right = self._insert(root.rigt, key)
        return root
    def pre_travels(self):
        if self.root is None:
            print(None)
        self._pre_treavels(self.root)
    def _pre_reavels(self,root):
        print(root.data)
        if root.left:
            self._pre_reavels(root.left)
        if root.right:
            self._pre_reavels(root.rigt)

    def update(self):
        pass
    def delete(self):
        pass

