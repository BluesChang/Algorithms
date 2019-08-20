import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            if cur_sum > res:
                res = cur_sum
        return res
