'''
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
解法一：基于Partition函数（即快排）的时间复杂度为O(n)的算法
'''


class Solution:
    def more_than_half_num(self, numbers):
        if not numbers:
            return
        middle = len(numbers) >> 1
        start = 0
        end = len(numbers) - 1
        index = self.partition(numbers, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.partition(numbers, start, end)
            else:
                start = index + 1
                index = self.partition(numbers, start, end)
        result = numbers[middle]
        return result

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
解法二：根据数组特点找出时间复杂度为O(n)的算法
'''


class Solution2:
    def more_than_half_num(self, numbers):
        if not numbers:
            return
        key, count = None, 0
        for num in numbers:
            if key is None:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1
            if count == 0:
                key = None
        return key
