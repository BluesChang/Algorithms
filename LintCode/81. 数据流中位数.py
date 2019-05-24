import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
        min = []
        max = []
        medians = []
        for num in nums:
            heapq.heappush(max, num)
            if len(max) - len(min) > 1:
                heapq.heappush(min, heapq.nlargest(1, max)[0])
            if len(max) > len(min):
                median = heapq.nlargest(1, max)[0]
                medians.append(median)
            else:
                median = heapq.nlargest(1, max)[0]
                medians.append(median)
        return medians
