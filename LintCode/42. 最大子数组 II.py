import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        length = len(nums)
        left_temp = nums[:]
        left = nums[:]
        for i in range(1, length):
            left_temp[i] = max(nums[i], nums[i] + left_temp[i - 1])
            left[i] = max(left[i - 1], left_temp[i])
        right_temp = nums[:]
        right = nums[:]
        for i in range(length - 2, -1, -1):
            right_temp[i] = max(nums[i], nums[i] + right_temp[i + 1])
            right[i] = max(right_temp[i], right[i + 1])
        greatest_sum = -sys.maxsize
        for i in range(length - 1):
            greatest_sum = max(left[i] + right[i + 1], greatest_sum)
        return greatest_sum
