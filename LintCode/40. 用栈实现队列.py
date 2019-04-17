class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(element)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        return self.stack1.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        return self.stack1[-1]
