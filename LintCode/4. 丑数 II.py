import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        ugly_number = set([1])
        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for multi in [2, 3, 5]:
                if val * multi not in ugly_number:
                    ugly_number.add(val * multi)
                    heapq.heappush(heap, val * multi)
        return val
