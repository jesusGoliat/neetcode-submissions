from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        i = 0
        while i < len(nums):
            if nums[i] in hash_map and abs(i-hash_map[nums[i]]) <= k:
                return True
            hash_map[nums[i]] = i
            i += 1
        return False