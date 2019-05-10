'''
题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第N个丑数。
例如6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当做是第一个丑数。
'''


class Solution:
    def get_ugly_number(self, index):
        if not index:
            return
        ugly_number = [1] * index
        next_ugly_index = 1
        multiply2 = multiply3 = multiply5 = 0
        while next_ugly_index < index:
            ugly_number[next_ugly_index] = min(ugly_number[multiply2] * 2, ugly_number[multiply3] * 3,
                                               ugly_number[multiply5] * 5)
            while ugly_number[multiply2] * 2 <= ugly_number[next_ugly_index]:
                multiply2 += 1
            while ugly_number[multiply3] * 3 <= ugly_number[next_ugly_index]:
                multiply3 += 1
            while ugly_number[multiply5] * 5 <= ugly_number[next_ugly_index]:
                multiply5 += 1
            next_ugly_index += 1
        return ugly_number[next_ugly_index - 1]
