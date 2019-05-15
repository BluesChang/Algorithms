'''
题目:一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，
请找出这个数字。
'''


class Solution:
    def get_missing_number(self, nums):
        if not nums:
            return
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] != mid:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                end = mid - 1
            else:
                start = mid + 1
        return -1
