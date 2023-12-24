# 示例使用
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
def dijkstra(graph,start,distances):
    visited = set()
    for current_node, weight in graph[start].item():
        if current_node not in visited:
            visited.add(current_node)
            if weight > distances[current_node]:
               continue
            elif weight + distances[start] < distances[current_node]:
                distances[current_node] = weight + distances[start]





if __name__ == '__main__':
   distance = dijkstra(graph_with_weights,'A')
   print(distance)


