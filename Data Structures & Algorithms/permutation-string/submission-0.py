class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_sub = [0]*26
        hash_check = [0]*26
        left = 0
        for x in s1:
            hash_sub[ord(x) - ord('a')] += 1
        for x in s2:
            idx = ord(x) - ord('a')
            hash_check[idx] += 1
            if hash_check == hash_sub:
                return True
            while hash_check[idx] > hash_sub[idx]:
                    hash_check[ord(s2[left]) - ord('a')] -= 1
                    left += 1
        return False