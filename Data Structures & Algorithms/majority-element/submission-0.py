class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0
        for x in nums:
            if count == 0:
                majority = x
                count += 1
            else:
                if x == majority:
                    count += 1
                else:
                    count -= 1
        return majority
            