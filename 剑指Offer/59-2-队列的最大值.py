'''
题目：请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back和pop_front的时间复杂度都是O(1)。
'''
from collections import deque


class QueueWithMax(object):
    def __init__(self):
        self.data = deque()
        self.max_queue = deque()
        self.current_index = 0

    def push_back(self, num):
        while len(self.max_queue) != 0 and num >= self.max_queue[-1][1]:
            self.max_queue.pop()
        self.max_queue.append((self.current_index, num))
        self.data.append((self.current_index, num))
        self.current_index += 1

    def pop_front(self):
        assert len(self.data) != 0
        index, num = self.data.popleft()
        if index == self.max_queue[0][0]:
            self.max_queue.popleft()

    def max(self):
        assert len(self.data) != 0
        return self.max_queue[0][1]
