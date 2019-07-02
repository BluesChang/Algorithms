'''
题目：
输入数字n，按顺序打印出从1到最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数999。
'''


class Solution:
    """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """

    def numbersByRecursion(self, n):
        # write your code here
        if n <= 0:
            return
        number = [0] * n
        for i in range(10):
            number[0] = str(i)
            self.print_to_max_of_n_digits_recursively(number, n, 0)

    def print_number(self, number):
        is_beginning_0 = True
        for i in range(len(number)):
            if is_beginning_0 and number[i] != '0':
                is_beginning_0 = False
            if not is_beginning_0:
                print('%c' % number[i])
        print('\t')

    def print_to_max_of_n_digits_recursively(self, number, length, index):
        if index == length - 1:
            self.print_number(number)
            return
        for i in range(10):
            number[index + 1] = str(i)
            self.print_to_max_of_n_digits_recursively(number, length, index + 1)


print(Solution().numbersByRecursion(3))
