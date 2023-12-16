# 并查集
class DisJoinSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self,i):
        if self.parent[i] ==i:
            return i
        self.find(self.parent[i])
    def union(self,i,j):
        root_i = self.find(i)
        root_j = self.find(j)
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
    def display(self):   # 打印不同的集合，打印不同集合的连通性
        # 怎么打印完全所有的集合
        pass




if __name__ == '__main__':
    for i in range (5):
        print(i)

# 集合的查找与合并,打印。
# 如何初始化一个并查集


