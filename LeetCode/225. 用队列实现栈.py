class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue2:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.queue1 and not self.queue2:
            return None

        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queue1 and not self.queue2:
            return None

        if self.queue1:
            return self.queue1[-1]
        else:
            return self.queue2[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
