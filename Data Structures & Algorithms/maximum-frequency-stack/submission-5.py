from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.hash_map = defaultdict(int)
        self.stack = []
    def push(self, val: int) -> None:
        self.hash_map[val] += 1
        freq = self.hash_map[val]
        if freq > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[freq - 1].append(val)
    def pop(self) -> int:
        val = self.stack[-1].pop()
        self.hash_map[val] -= 1
        if not self.stack[-1]:
            self.stack.pop()
        return val
            
        