# 最小生成树算法



# 想清楚解题思路
# 1.
def kruskal(graph,start):
    edge = []
    parent = []
    min_tree = []
    for key in graph:
        for neighbor,weight in  graph[key].items():
           edge.append((key,neighbor,weight))
    edge.sort()

    def find(node):
       if parent[node] != node:
          return find(parent[node])
    def union(node1,node2):
       root1 = find(node1)
       root2 = find(node2)
       parent[root2] = root1

    while edge:
       node1,node2,weight = edge.pop()
       if find(node1) != find(node2):
           min_tree.append((node1,node2,weight))
           union(node1,node2)
    return min_tree


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 1, 'B': 3, 'D': 2},
    'D': {'B': 1, 'C': 2}
}
if __name__ == '__main__':
    print(kruskal(graph,'A'))