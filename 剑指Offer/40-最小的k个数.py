'''
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
'''
解法一：时间复杂度为O(n)的算法，只有当我们可以修改输入的数组时可用
'''


class Solution:
    def get_least_numbers(self, numbers, k):
        if not numbers or k <= 0 or k > len(numbers):
            return
        start = 0
        end = len(numbers) - 1
        index = self.partition(numbers, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(numbers, start, end)
            else:
                start = index + 1
                index = self.partition(numbers, start, end)
        return numbers[:k]

    def partition(self, numbers, start, end):
        key = numbers[end]
        i = start - 1
        for j in range(start, end):
            if numbers[j] <= key:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i + 1], numbers[end] = numbers[end], numbers[i + 1]
        return i + 1


'''
解法二：时间复杂度为O(nlogk)的算法，特别适合处理海量数据
'''
import heapq


class Solution2:
    def get_least_numbers(self, numbers, k):
        if not numbers or k <= 0 or k > len(numbers):
            return
        heaps = []
        result = []
        for i in numbers:
            heapq.heappush(heaps, i)
        for i in range(k):
            result.append(heapq.heappop(heaps))
        return result
