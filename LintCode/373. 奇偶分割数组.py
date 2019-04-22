class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return
        begin = 0
        end = len(nums) - 1
        while begin < end:
            while begin < end and (nums[begin] & 0x1) != 0:
                begin += 1
            while begin < end and (nums[end] & 0x1) == 0:
                end -= 1
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
