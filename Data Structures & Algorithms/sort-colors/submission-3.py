class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #We use two pointer pattern -> RED <-> WHITE <-> BLUE
        red = 0
        i = 0
        blue = len(nums) - 1
        while i <= blue:
            if nums[i] == 2:
                nums[i],nums[blue] = nums[blue],nums[i]
                blue -= 1
            elif nums[i] == 0 and i > red:
                nums[i],nums[red] = nums[red],nums[i]
                red += 1
            else:
                i += 1