class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for x in nums:
            if x in check:
                return True
            check.add(x)
        return False