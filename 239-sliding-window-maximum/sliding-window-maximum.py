class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)

    def appendleft(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty deque")
        return self.items.pop()

    def popleft(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty deque")
        return self.items.pop(0)

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty deque")
        return self.items[0]

    def peek_back(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty deque")
        return self.items[-1]

    def __str__(self):
        return str(self.items)

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        dq = Deque()
        ans = []
        for i in range(len(arr)):
            if not dq.is_empty() and dq.peek_front() == i - k:
                dq.popleft()
            while not dq.is_empty() and arr[dq.peek_back()] < arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(arr[dq.peek_front()])
        return ans

        
        