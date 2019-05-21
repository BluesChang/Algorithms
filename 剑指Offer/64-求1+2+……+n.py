'''
题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''
方法一：python式写法
'''
class Solution:
    def sum_solution(self, n):
        return sum(range(n + 1))

'''
方法二：利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反运算，
那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。
'''
class Solution2:
    def sum_solution(self, n):
        return self.sum(n)

    def sum0(self, n):
        return 0

    def sum(self, n):
        fun = {False: self.sum0, True: self.sum}
        return n + fun[not not n](n - 1)
