class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.data_stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.data_stack.append(number)
        if len(self.min_stack) == 0 or number < self.min_stack[-1]:
            self.min_stack.append(number)
        else:
            self.min_stack.append(self.min_stack[-1])

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if len(self.data_stack) == 0 and len(self.min_stack) == 0:
            return None
        if len(self.data_stack) > 0 and len(self.min_stack) > 0:
            self.min_stack.pop()
            return self.data_stack.pop()

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.min_stack[-1]
