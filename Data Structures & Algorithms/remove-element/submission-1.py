#We can use the two pointers pattern:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            if nums[start] == val:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
            else:
                start += 1
        if nums[start] == val:
            return start
        else:
            return start + 1