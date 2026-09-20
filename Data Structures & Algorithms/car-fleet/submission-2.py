class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            stack.append((position[i],time))
        stack.sort()
        i = 0
        while i < len(position):
            i += 1
            result += 1
            _,time = stack.pop()
            while stack and stack[-1][1] <= time:
                stack.pop()
                i += 1
        return result