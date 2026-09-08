from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #We make a prefix-array
        count = 0
        prefix = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            prefix.append(prefix[i-1] + nums[i])
        rest = defaultdict(int)
        rest[0] = 1
        for x in prefix:
            if (x - k) in rest:
                count += rest[x-k]
            rest[x] += 1
        return count
                