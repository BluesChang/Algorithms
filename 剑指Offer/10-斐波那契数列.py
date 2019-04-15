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
        for i in range(2,n+1):
            result.append(result[i-1]+result[i-2])
        return result[n]

#最优写法 时间O（logn）
import numpy as np
def Fibonacci_Matrix(n):
    result_list = []
    Matrix = np.matrix('1 1;1 0')
    for i in range(0, n):
        result_list.append(np.array(pow(Matrix, i))[0][0])
    return result_list

