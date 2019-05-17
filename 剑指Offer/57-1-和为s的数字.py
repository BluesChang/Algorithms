'''
题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，输出任意一对即可。
'''


class Solution:
    def find_numbers_with_sum(self, data, sum):
        if not data:
            return
        ahead = len(data) - 1
        behind = 0
        while behind < ahead:
            cur_sum = data[ahead] + data[behind]
            if cur_sum == sum:
                return behind, ahead
            elif cur_sum > sum:
                ahead -= 1
            else:
                behind += 1
        return
