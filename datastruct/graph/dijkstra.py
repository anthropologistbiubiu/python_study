# 示例使用
from collections import deque
import heapq
graph_with_weights = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 7},
    'C': {'A': 4, 'F': 5, 'G': 2},
    'D': {'B': 2},
    'E': {'B': 7, 'H': 1},
    'F': {'C': 5},
    'G': {'C': 2},
    'H': {'E': 1}
}
# 初始化最短距离
# 把邻接的节点开始加入到堆中
# 开始比较已知最短路径与源节点到当前节点的的距离，如果小于则更新源节点到其他节点的最短距离，如果不小于则不需要通过当前节点来更新
# 重复以上步骤

# 没有想明白为什么要用堆这个结构，直接用队列不可以吗？
# 是在遍历的过程中更新，还是在更新最短路径的过程中遍历。
# 那总得有个遍历的顺序,要么就按照广度优先遍历的顺序去完成。
# 优化一下，使用更人性化的方式对这个距离进行记录
# 是否有必要使用set() 这个集合对已经访问过的节点再去访问。
# 其次为什么要用heap 来记录这个访问的过程，而不是队列。

def dijkstra(graph,start,distances):
    visited = set()
    queue = deque()
    queue.append(start)
    distances[start] = 0
    while queue:
        current_node = queue.popleft()
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if weight > distances[neighbor]:
                    continue
                elif weight + distances[current_node] < distances[neighbor]:
                    distances[neighbor] = weight + distances[current_node]


# 优化版本
# 贪心的策略是体现在选择中继节点的时候，选择最短的距离，然后遍历完全整个优先级队列。
def dfs_with_heap(graph,start):
    distances = {node:float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(start,0)]
    while priority_queue:
        current_node, current_distance = heapq.heappop(priority_queue)
        if distances[current_node] < current_distance:
            continue
        for neighbor,weight in graph[current_node].items():
           distance =  current_distance + weight
           if distance < distances[neighbor]:
               distances[neighbor] = distance
               heapq.heappush(priority_queue,(neighbor,distance))
    return distances

if __name__ == '__main__':
    distances ={node:float('infinity') for node in graph_with_weights}
    dijkstra(graph_with_weights, 'A',distances)
    print(distances)
    print(dfs_with_heap(graph_with_weights,'A'))
