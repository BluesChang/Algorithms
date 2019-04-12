'''
题目1：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


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
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if self.stack2:
            self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if self.stack2:
            self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()