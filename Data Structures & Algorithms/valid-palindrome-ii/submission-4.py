#s is made up of only lowercase English letters.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        deletion = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif deletion:
                if left + 1 >= right:
                    return True
                elif s[left] == s[right - 1] and s[left + 1] == s[right - 2]:
                    right -= 1
                else:
                    left += 1
                deletion = False
            else:
                return False
        
        return True
                