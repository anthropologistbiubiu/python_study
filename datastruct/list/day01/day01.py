
# 写一个链表的增删改查操作
class Node:
    def __int__(self,data=None):
       self.data = data
       self.next = Node

class LinkList:
    def __int__(self):
        self.head = None
    # 插入节点
    def append(self,data):
        new_node = Node(data)
        if not self.head:
           self.head = new_node
           return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node # 尾插法

    def delete(self,data):
        last_node = self.head
        if last_node.data == data:
            self.head = self.head.next
        while last_node.next.data != data:
            last_node = last_node.next
        if last_node is None:
            return
        last_node.next = last_node.next.next



