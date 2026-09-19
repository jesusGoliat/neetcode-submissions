class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if x < 0:
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(x):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(x)
                elif abs(stack[-1]) == abs(x):
                    stack.pop()
            else:
                stack.append(x)
        return stack