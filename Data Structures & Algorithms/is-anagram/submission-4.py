from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Because we use only letter
        check = [0]*26
        for c in s:
            check[ord(c) - ord('a')] += 1
        for c in t:
            check[ord(c) - ord('a')] -= 1
        for x in check:
            if x != 0:
                return False
        return True
            