


class SegmentNode:
    def __init__(self,start,end) -> None:
        self.total = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class SegmentNodeTree:
    def __init__(self,nums) -> None:
        self.nums = nums
        self.root = self.buildSegmentTree()

    def buildSegmentTree(self):
        self._buildSegmentTree(0,len(self.nums)-1)

    def _buildSegmentTree(self,start,end):

        if start > end:
            return None

        if start == end:
            node = SegmentNode(start,end)
            node.total = self.nums[end]
            return node
        mid = (start + end) // 2
        left_node = self._buildSegmentTree(start,mid)
        right_node = self._buildSegmentTree(mid+1,end)
        # 退栈空间的内存操作
        node = SegmentNode(start,end)
        node.total = left_node.total + right_node.total
        node.left = left_node
        node.right = right_node
        return node




    def range_sum(self,start,end):
        self._range_sum(self.root,start,end)
    def _range_sum(self,root,start,end):
        if root.start == start and root.end == end:
            return root.total
        mid = (root.start + root.end) // 2
        if start > mid:
            return self._range_sum(root.right,start,end)
        elif end < mid:
            return self._range_sum(root.left,start,end)
        return self._range_sum(root.left,start,mid) + self._range_sum(root.right,mid+1,end)


def main():
    nums = [1,2,3,4,5,6,7]
    segmentTree1 = SegmentNodeTree(nums)
    print(segmentTree1.root)
    segmentTree1.buildSegmentTree()
    print(segmentTree1.range_sum(1,2))

if __name__ == '__main__':
    main()
