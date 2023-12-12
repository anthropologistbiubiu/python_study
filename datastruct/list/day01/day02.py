class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 插入节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    # 删除节点
    def delete(self, data):
        current_node = self.head
        # 处理头节点
        if current_node and current_node.data == data:
            self.head = current_node.next_node
            current_node = None
            return

        # 处理非头节点
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next_node

        if current_node is None:
            return
        prev_node.next_node = current_node.next_node
        current_node = None

    # 修改节点
    def update(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
                return
            current_node = current_node.next_node

    # 查找节点
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    # 打印链表
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

# 示例用法
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.display()

my_linked_list.delete(2)
my_linked_list.display()

my_linked_list.update(1, 10)
my_linked_list.display()

print(my_linked_list.search(3))  # 输出 True
print(my_linked_list.search(5))  # 输出 False
