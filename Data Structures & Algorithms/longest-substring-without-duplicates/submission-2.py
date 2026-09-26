class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {} #We use the dict to jump directly 
        result = left = 0
        for i, x in enumerate(s):
            if x in last and last[x] >= left:
                left = last[x] + 1
            last[x] = i
            result = max(result, i - left + 1)
        return result