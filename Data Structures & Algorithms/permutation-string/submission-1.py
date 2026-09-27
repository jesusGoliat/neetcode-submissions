class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_sub = [0]*26
        hash_check = [0]*26
        left = 0
        check = 0
        count = 0
        for x in s1:
            hash_sub[ord(x) - ord('a')] += 1
        for x in hash_sub:
            if x > 0:
                count += 1
        for x in s2:
            pos = ord(x) - ord('a')
            hash_check[pos] += 1
            if hash_check[pos] == hash_sub[pos]:
                check += 1
            if check == count:
                return True
            while hash_check[pos] > hash_sub[pos]:
                idx = ord(s2[left]) - ord('a')
                hash_check[idx] -= 1
                if hash_check[idx] == 0 and check > 0:
                    check -= 1
                left += 1
        return False