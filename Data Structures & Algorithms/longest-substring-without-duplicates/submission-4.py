class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        result = 0
        left = 0
        for x in s:
            while x in unique:
                unique.remove(s[left])
                left += 1
            unique.add(x)
            result = max(result,len(unique))
        return result
            