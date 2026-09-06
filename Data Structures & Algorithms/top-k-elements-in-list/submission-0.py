from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each number
        count = Counter(nums)
        
        # 2. Create buckets where the index represents the frequency.
        # The max frequency is len(nums), so we need an array of size len(nums) + 1.
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 3. Group numbers by their frequency
        for num, c in count.items():
            freq[c].append(num)
            
        # 4. Gather the top k elements by iterating backwards (highest frequency to lowest)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res