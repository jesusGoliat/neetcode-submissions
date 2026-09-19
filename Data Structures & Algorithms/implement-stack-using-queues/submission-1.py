from collections import deque #We can use only .append() and popleft() and if it's empty
class MyStack:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        self.queue.append(x)
        n = len(self.queue)
        for i in range(1,n): #We have to remove and append n-1 times
            self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return True if not self.queue else False
    