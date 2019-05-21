'''
题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''
此题主要针对C++。
'''


class Solution:
    def sum_solution(self, n):
        return sum(range(n + 1))
