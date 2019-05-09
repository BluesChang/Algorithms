'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接处的所有数字中最小的一个。例如，输入数组{33,32,321}，则打印出这3个数字能
排成的最小数字321323。
'''
from functools import cmp_to_key


class Solution:
    """
    @param nums: n non-negative integer array
    @return: A string
    """

    def min_number(self, nums):
        # write your code here
        if not nums:
            return
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'
