class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = [(target - p) / s for p, s in cars]
        result = 0

        while stack:
            time = stack.pop()
            result += 1
            while stack and stack[-1] <= time:
                stack.pop()

        return result