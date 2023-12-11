
# 写一个链表的增删改查操作
class Node:
    def __init__(self,data=None):
       self.data = data
       self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.capacity = 0
    # 插入节点
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
           return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node # 尾插法
        self.capacity+=1

    def delete(self,data):
        cur_node = self.head
        if cur_node is None:
            return
        # 单独处理头节点
        if cur_node.data == data:
            self.head = self.head.next
            self.capacity+=1
        # 处理非头节点
        while cur_node.next and cur_node.next.data != data:
            cur_node = cur_node.next
        if cur_node.next is None:
            return
        cur_node.next = cur_node.next.next
        self.capacity+=1
    def update(self):
        cur_node = self.head
        if cur_node is None:
            return

        pass
    def index(self,index):
        cur_node = self.head
        if cur_node is None:
            return
        if index >= self.capacity or index < 0:
            return
        else:
            i = 0
            while i < index:
                cur_node= cur_node.next
                i+=1
            return cur_node.data
        pass
    def reverse(self):
        pass
    def sort(self):
        pass
    def didsplay(self):
       cur = self.head
       while cur:
           print(cur.data)
           cur = cur.next


mylist = LinkList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.didsplay()

mylist.delete(1)
print("delete 1")
mylist.didsplay()
mylist.delete(4)
print("delete 4")
mylist.didsplay()
print("delete 3")
mylist.delete(3)
mylist.didsplay()
print('mylist.index')
print(mylist.index(0))
