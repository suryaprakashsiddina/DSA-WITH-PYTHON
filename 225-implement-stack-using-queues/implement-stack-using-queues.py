class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None


class MyStack:

    def __init__(self):
        self.q = Queue()
        

    def push(self, x: int) -> None:
        self.q.enqueue(x)
        for _ in range(self.q.size() - 1):
            self.q.enqueue(self.q.dequeue())
        

    def pop(self) -> int:
        return self.q.dequeue()
        

    def top(self) -> int:
        return self.q.front()
        

    def empty(self) -> bool:
        return self.q.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()