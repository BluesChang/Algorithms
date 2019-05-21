'''
题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。
'''


class Solution:
    def multiply(self, a):
        if not a:
            return
        length = len(a)
        b = [1] * length
        for i in range(1, length):
            b[i] = b[i - 1] * a[i - 1]
        tmp = 1
        for i in range(length - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b
