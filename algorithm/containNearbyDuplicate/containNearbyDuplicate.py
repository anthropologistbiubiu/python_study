


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for index, num in enumerate(nums):
            if num in hash_table and index - hash_table[num] <= k:
                return True
            # 无论是否找到满足条件的重复项，都更新索引
            hash_table[num] = index
        return False
