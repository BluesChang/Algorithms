'''
题目：给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。例如，如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}，
'''

'''
方法一：蛮力法
'''


class Solution:
    def max_in_windows(self, nums, size):
        if not nums or not size or size > len(nums):
            return
        return [max(nums[i:i + size]) for i in range(len(nums) - size + 1)]


'''
方法二：双向队列
'''
import collections


class Solution2:
    def max_in_windows(self, nums, size):
        max_in_windows = []
        if nums and 1 <= size <= len(nums):
            index = collections.deque()
            for i in range(size):
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                index.append(i)
            for i in range(size, len(nums)):
                max_in_windows.append(nums[index[0]])
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                if index and index[0] <= i - size:
                    index.popleft()
                index.append(i)
            max_in_windows.append(nums[index.popleft()])
        else:
            return []
        return max_in_windows
