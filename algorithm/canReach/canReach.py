from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = []
        exist = set()
        queue.append(start)
        while queue is not None:
            elem = queue.pop()
            print(elem)
            if arr[elem] == 0:
                return True
            if elem in exist:
                continue
            if start - arr[start] > 0:
                queue.append(start - arr[start])
            if start + arr[start] < len(arr) - 1:
                queue.append(start + arr[start])
        return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

solution = Solution()
print(solution.canReach(arr, start))
