#First Solution with O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        result = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min(result,right-left+1)
                total -= nums[left]
                left += 1
        return result if result != float('inf') else 0
                
                
            
            
            