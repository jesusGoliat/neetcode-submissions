class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k   # possible window starts: [0, n-k]

        while left < right:
            mid = (left + right) // 2
            # Compare the distance to the window's left end vs. the element just past its right end
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1   # window should shift right
            else:
                right = mid      # keep this start or go left (ties favor the smaller values)

        return arr[left:left + k]