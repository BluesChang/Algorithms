'''
题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖交易该股票可能获得的利润是多少？例如一只股票在某些时间节点的价格为{9, 11, 8, 5,
7, 12, 16, 14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
'''


class Solution:
    def max_diff(self, nums):
        if not nums and len(nums) < 2:
            return 0
        min = nums[0]
        max_diff = nums[1] - min
        for i in range(2, len(nums)):
            if nums[i - 1] < min:
                min = nums[i - 1]
            cur_diff = nums[i] - min
            if cur_diff > max_diff:
                max_diff = cur_diff
        return max_diff
