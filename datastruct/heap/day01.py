class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()

    def pop(self):
        if len(self.heap) == 0:
            return None
        top_item = self.heap[0]
        self._heapify_down()
        return top_item

    def _heapify_up(self):
        # 想清楚堆想上调整的过程中的思路
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index-1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self._swap(parent_index, index)
            else:
                break


    def _heapify_down(self):
        pass
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def display(self):
        # 如何打印出堆的结构形状
        pass
