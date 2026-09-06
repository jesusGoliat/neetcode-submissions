import random
class Solution:
    def partition(self,start,end,nums):
        new_pivot = random.randint(start,end)
        nums[end],nums[new_pivot] = nums[new_pivot],nums[end]
        pivot = nums[end]
        i = start - 1
        for j in range(start,end):
            if nums[j] < pivot:
                i += 1
                nums[j],nums[i] = nums[i],nums[j]
        i += 1
        nums[i],nums[end] = nums[end],nums[i]
        return i
    def quicksort(self,start,end,nums):
        if start >= end:
            return
        p = self.partition(start,end,nums)
        self.quicksort(start,p-1,nums)
        self.quicksort(p+1,end,nums)
                
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.quicksort(0,len(nums)-1,nums)
        return nums