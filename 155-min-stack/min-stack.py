class MinStack:

    def __init__(self):
        self.st = []
        self.mini = float('inf')
        

    def push(self, val: int) -> None:
        value = val
        if not self.st:
            self.mini = value
            self.st.append(value)
        else:
            if value >= self.mini:
                self.st.append(value)
            else:
                self.st.append(2*value - self.mini)
                self.mini = value
        

    def pop(self) -> None:
        if not self.st:
            return
        el = self.st.pop()
        if el < self.mini:
            self.mini = 2*self.mini - el
        

    def top(self) -> int:
        if not self.st:
            return -1
        el = self.st[-1]
        if el < self.mini:
            return int(self.mini)
        else:
            return int(el)
        

    def getMin(self) -> int:
        return int(self.mini)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()