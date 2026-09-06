class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        n = len(nums)
        for i in range(n):
            rest = target - nums[i]
            
            if rest in diff:
                return [diff[rest],i]
            
            diff[nums[i]] = i