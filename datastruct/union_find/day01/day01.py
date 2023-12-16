# 并查集
class DisJoinSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    def find(self,i):
        print(i)
        pass
    def union(self,i,j):
        print(i,j)
        pass
    def display(self):   # 打印不同的集合，打印不同集合的连通性
        pass




if __name__ == '__main__':
    for i in range (5):
        print(i)

# 集合的查找与合并,打印。
# 如何初始化一个并查集


