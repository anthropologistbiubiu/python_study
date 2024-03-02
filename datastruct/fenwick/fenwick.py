
class BinaryIndexTree:
    def __init__(self,nums):
        self.tree = []
        for index,item in nums:
            self.update(index+1,item)

    def update(self,index,item):
        self.tree[index] += item
        index += self.lowbit(index)

    def lowbit(self,x):
        return x & -x

    def query(self,index):
        total = 0
        while index> 0:
            total += self.tree[index]
            index -= self.lowbit(index)
    def query_rang(self,end,start):
        return self.query(end) - self.query(start-1)


def main():
    nums = [1,3,5,7,9,10,22,5]
    bit = BinaryIndexTree(nums)
    print(bit.query(2))
    print(bit.query_rang(1,5))


if __name__ == '__main__':
    main()