class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res_left = []
        res_right = []
        #We find the last element that is a <= x
        n = len(arr) - 1
        left = 0
        right = n
        while left < right:
            mid = ((left + right) // 2) + 1 # It's to find the last element
            if arr[mid] <= x:
                left = mid
            else:
                right = mid - 1
        right += 1
        for i in range(k):
            if right > n or (left >= 0 and abs(x-arr[left]) <= abs(x-arr[right])):
                res_left.append(arr[left])
                left -= 1
            else:
                res_right.append(arr[right])
                right += 1
        res_left.reverse()
        return res_left + res_right