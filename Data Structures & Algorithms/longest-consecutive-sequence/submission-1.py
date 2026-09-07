#We want start to count only if we find the start of a sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #Remember it doesn't matter the order
        longest = 0
        for num in numSet:
            if not (num-1) in numSet: #We find the start of a sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                
                longest = max(longest,length)
        return longest
        