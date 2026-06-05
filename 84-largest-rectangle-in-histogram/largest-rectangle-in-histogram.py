class Stack:
    """A basic stack implementation using a list."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self.items[-1]

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = Stack()
        n = len(heights)
        maxA = 0

        for i in range(n+1):
            while not st.is_empty() and (i == n or heights[st.peek()] > heights[i]):
                height = heights[st.peek()]
                st.pop() # because we want the left smallest element thats why we are poping the element
                width = 0
                if st.is_empty():
                    width = i
                else:
                    width = i - st.peek() - 1
                maxA = max(maxA, width * height)
            st.push(i)
        return maxA        