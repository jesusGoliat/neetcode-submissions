class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            val = nums[i]
            while 0 < val <= n and nums[val - 1] != val:
                nums[i], nums[val - 1] = nums[val - 1], nums[i]
                val = nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1