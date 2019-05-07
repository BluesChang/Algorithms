'''
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
import heapq


class Solution:
    min = []
    max = []

    def insert_num(num):
        if not num:
            return
        heapq.heappush(max, num)
        if len(max) - len(min) > 1:
            heapq.heappush(min, heapq.heappop(max))

    def get_median():
        if len(max) > len(min):
            median = float(max[0])
        else:
            median = (max[0] + min[-1]) / 2
        return median
