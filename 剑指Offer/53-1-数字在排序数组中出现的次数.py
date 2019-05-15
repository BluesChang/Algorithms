'''
题目：统计一个数字在排序数组中出现的次数。例如，输入排序数组{1,2,3,3,3,3,4,5,}和数字3，由于3在这个数组中出现了4次，因此输出4。
'''


class Solution:
    def get_number_of_k(self, data, k):
        if len(data) == 0:
            return 0
        start = 0
        end = len(data) - 1
        first = self.get_first_k(data, k, start, end)
        if first == -1:
            return 0
        last = self.get_end_k(data, k, first, end)
        number = last - first + 1
        return number

    def get_first_k(self, data, k, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if data[mid] < k:
                start = mid
            else:
                end = mid
        if data[start] == k:
            first = start
        elif data[end] == k:
            first = end
        else:
            first = -1
        return first

    def get_end_k(self, data, k, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if data[mid] <= k:
                start = mid
            else:
                end = mid
        if data[end] == k:
            last = end
        else:
            last = start
        return last
