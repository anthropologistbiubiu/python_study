from collections import defaultdict

class UndirectedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def __str__(self):
        result = ""
        for vertex, neighbors in self.adj_list.items():
            result += f"{vertex}: {', '.join(map(str, neighbors))}\n"
        return result

# Example usage:
graph = UndirectedGraph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
print(graph)
