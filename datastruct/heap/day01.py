class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()
        self.size +=1

    def pop(self):
        if len(self.heap) == 0:
            return None
        top_item = self.heap[0]
        self._swap(0,self.size-1)
        self.size -= 1
        self._heapify_down()
        return top_item

    def _heapify_up(self):
        # 想清楚堆想上调整的过程中的思路
        index = len(self.heap) - 1
        while index >= 0:
            parent_index = (index-1) // 2
            if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
                self._swap(parent_index, index)
            else:
                break
            index = parent_index

    def _heapify_down(self):
        last_index = len(self.heap) -1
        cur_index = 0
        while cur_index*2+1 < self.size:
            left_index = cur_index*2 +1
            right_index = cur_index*2 +2
            print(left_index,right_index)
            if right_index < self.size and self.heap[right_index] < self.heap[left_index]:
                min_index = right_index
            else:
                min_index = left_index
            if self.heap[min_index] < self.heap[cur_index]:
                self._swap(min_index,cur_index)
            cur_index = min_index

    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def display(self):
        # 如何打印出堆的结构形状
        print(self.heap[:self.size])


myheap = MinHeap()
myheap.push(8)
myheap.push(3)
myheap.push(4)
myheap.push(6)
myheap.push(1)
myheap.push(2)
myheap.pop()
myheap.display()
