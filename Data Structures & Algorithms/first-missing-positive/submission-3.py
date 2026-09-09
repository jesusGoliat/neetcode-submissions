class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Use n+1 as a neutral placeholder instead of 0/negatives,
        # since n+1 is never a candidate answer's target index anyway
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            val = abs(nums[i]) #This is for the case we already marked this cell
            if 1 <= val <= n and nums[val - 1] > 0: #We can have repeteaded numbers and have marked already some cell
                nums[val - 1] = -nums[val - 1]

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1