class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left = 0
        right = len(people) - 1
        while left < right:
            value = people[left] + people[right]
            if value > limit:
                right -=1
            else:
                left += 1
                right -= 1
            count += 1
        if left == right:
            count += 1
        return count