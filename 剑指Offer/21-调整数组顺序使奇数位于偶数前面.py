'''
题目：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''
import unittest

class Solution:
    """
    @param: nums: an array of integers
    """
    def reorder_odd_even(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return
        begin = 0
        end = len(nums) - 1
        while begin < end:
            while begin < end and (nums[begin] & 0x1) ==1:
                begin += 1
            while begin < end and (nums[end] & 0x1) == 0:
                end -= 1
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
        return nums


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 3, 2, 4],Solution().reorder_odd_even([1,2,3,4]))

Test().test()
