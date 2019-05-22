from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        max_in_windows = []
        if nums and 1 <= k <= len(nums):
            index = deque()
            for i in range(k):
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                index.append(i)
            for i in range(k, len(nums)):
                max_in_windows.append(nums[index[0]])
                while index and nums[i] >= nums[index[-1]]:
                    index.pop()
                if index and index[0] <= i - k:
                    index.popleft()
                index.append(i)
            max_in_windows.append(nums[index.popleft()])
        else:
            return []
        return max_in_windows
