from collections import deque


class RecentCounter:

    def __init__(self):
        self.ping_queue = deque([])

    def ping(self, t: int) -> int:
        self.ping_queue.append(t)
        while t - self.ping_queue[0] > 3000:
            self.ping_queue.popleft()
        return len(self.ping_queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
