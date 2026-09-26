class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_freq = 0
        result = 0
        left = 0
        for right, x in enumerate(s):
            idx = ord(x) - ord('A')
            count[idx] += 1
            max_freq = max(max_freq, count[idx])
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result