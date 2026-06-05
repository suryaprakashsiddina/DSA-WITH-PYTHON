class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class MyQueue:

    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        
    def push(self, x: int) -> None:
        self.input.push(x)
        

    def pop(self) -> int:
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())
        return self.output.pop()
        

    def peek(self) -> int:
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())
        return self.output.top()
        

    def empty(self) -> bool:
        return self.input.is_empty() and self.output.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()