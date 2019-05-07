'''
题目：输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
'''
import sys


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return None
        current_sum = 0
        greatest_sum = -sys.maxsize
        for i in range(len(nums)):
            if current_sum <= 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            if greatest_sum < current_sum:
                greatest_sum = current_sum
        return greatest_sum


class Solution2:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
