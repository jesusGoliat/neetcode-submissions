class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        count = 0
        left = 0
        value = nums[0]
        while count < n:
            value = nums[left]
            right = (left + k)%n
            while right != left:
                value,nums[right] = nums[right],value
                right = (right + k) %n
                count += 1
            nums[right] = value
            left += 1
            count += 1  