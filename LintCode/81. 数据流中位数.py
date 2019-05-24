import heapq


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def medianII(self, nums):
        self.min = []
        self.max = []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(-self.max[0])
        return medians

    def add(self, value):
        if len(self.max) <= len(self.min):
            heapq.heappush(self.max, -value)
        else:
            heapq.heappush(self.min, value)

        if len(self.min) == 0 or len(self.max) == 0:
            return
        if -self.max[0] > self.min[0]:
            heapq.heappush(self.max, -heapq.heappop(self.min))
            heapq.heappush(self.min, -heapq.heappop(self.max))
