
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
        cur_node = self.head
        # 单独处理头节点
        if cur_node.data == data:
            self.head = self.head.next
        # 处理非头节点
        while cur_node.next.data != data:
            cur_node.next = cur_node.next.next
        if cur_node is None:
            return
        cur_node.next = cur_node.next.next
    def didsplay(self):
       cur = self.head
       while cur:
           print(cur.data)
           cur = cur.next


