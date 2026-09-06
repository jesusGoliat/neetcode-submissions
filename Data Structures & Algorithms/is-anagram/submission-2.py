from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = defaultdict(int)
        check_t = defaultdict(int)
        result = 0
        for c in s:
            check_s[c] += 1
        for c in t:
            check_t[c] += 1
        
        return check_s == check_t
            