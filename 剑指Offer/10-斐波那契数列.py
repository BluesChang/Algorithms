'''
题目一：求斐波那契数列的第n项
'''


class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])
            return result[n]


# 最优写法 时间O（logn）
import numpy as np


def Fibonacci_Matrix(n):
    Matrix = np.matrix('1 1;1 0')
    if n == 1:
        return Matrix
    if n == 2:
        return pow(Matrix, 2)
    elif n % 2 == 1:
        return pow(Fibonacci_Matrix((n - 1) / 2), 2) * Matrix
    else:
        return pow(Fibonacci_Matrix(n / 2), 2)


'''
题目二：青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
解法：
其实就是斐波那契数列
'''


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        result = [1, 1]

        if n == 0:
            return 0

        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])

        return result[n]
