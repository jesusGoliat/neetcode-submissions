class MyQueue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    def push(self, x: int) -> None:
        self.stack_push.append(x)
    def pop(self) -> int:
        value = self.peek()
        self.stack_pop.pop()
        return value
            
    def peek(self) -> int:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return not (self.stack_push or self.stack_pop)

        