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
            elif hash_check[pos] == hash_sub[pos] + 1:
                check -= 1  # just overshot a previous match
            if check == count:
                return True
            while hash_check[pos] > hash_sub[pos]:
                idx = ord(s2[left]) - ord('a')
                if hash_check[idx] == hash_sub[idx]:
                    check -= 1  # about to break a match
                hash_check[idx] -= 1
                if hash_check[idx] == hash_sub[idx]:
                    check += 1  # decrementing landed exactly on a match
                left += 1
        return False