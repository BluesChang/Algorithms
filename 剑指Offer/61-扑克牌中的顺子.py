'''
题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
'''


class Solution:
    def is_continuous(self, nums):
        if not nums:
            return False
        nums = sorted(nums)
        # 统计数组中0的个数
        num_of_zero = len([i for i in nums if i == 0])
        num_of_gap = 0
        # 统计数组中的间隔数目
        small = num_of_zero
        big = small + 1
        while big < len(nums):
            if nums[small] == nums[big]:
                return False
            num_of_gap += nums[big] - nums[small] - 1
            small += 1
            big += 1
        return False if num_of_gap > num_of_zero else True
