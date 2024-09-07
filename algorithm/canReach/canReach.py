from typing import List
import queue


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = queue.Queue()
        exist = set()
        q.put(start)
        while not q.empty():
            #arr = [4, 4, 1, 3, 0, 3]
            elem = q.get()
            if arr[elem] == 0:
                return True
            if elem in exist:
                continue
            else:
                exist.add(elem)
            if elem - arr[elem] >= 0:
                q.put(elem - arr[elem])
            if elem + arr[elem] < len(arr):
                q.put(elem + arr[elem])
        return False



arr = [4, 4, 1, 3, 0, 3]
start = 2
solution = Solution()
print(solution.canReach(arr, start))

