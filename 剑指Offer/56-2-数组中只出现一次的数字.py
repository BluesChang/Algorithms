'''
题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
'''


class Solution:
    def find_number_appearing_once(self, nums):
        if not nums:
            return
        bit_sum = [0] * 32
        for num in nums:
            for i in range(32):
                if ((1 << i) & num) != 0:
                    bit_sum[i] += 1
        res = 0
        for i in range(32):
            if (bit_sum[i] % 3) == 1:
                res += 1 << i
        return res
