'''
题目：用两个栈来实现一个队列，完成队列的Push、Pop、Top操作。
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


'''
题目：用两个队列实现一个栈，完成栈的Push、Pop操作。
'''


class QueueToStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, element):
        if self.queue2:
            self.queue2.append(element)
        else:
            self.queue1.append(element)

    def pop(self):
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
