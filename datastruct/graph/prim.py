 import heapq
# 最小生成树算法

# 给出prime 算法的
# 首先从任意节点开始,把邻节点的权重都加入到一个堆中。
# 然后从相邻节点找权重最小的边加入到最小生成树中
# 直到把所有的节点都加入到生成树中







def prim(graph,start):
    visited = set()
    visited.add(start)
    heap = []
    heapq.heapify(heap)
    for neighbor ,weight in graph[start].items():
        heapq.heappush(heap,heap)
    while heap:
        min_weight = heapq.heappop(heap)



if __name__ == '__main__':
    prim()







