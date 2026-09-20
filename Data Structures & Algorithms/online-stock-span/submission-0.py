class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _,value = self.stack.pop()
            span += value
        self.stack.append((price,span))
        return span
        
