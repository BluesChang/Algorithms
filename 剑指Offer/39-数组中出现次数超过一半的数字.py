'''
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
解法一：基于Partition函数（即快排）的时间复杂度为O(n)的算法
'''
'''
解法二：根据数组特点找出时间复杂度为O(n)的算法
'''


class Solution:
    def more_than_half_num(self, numbers):
        key, count = None, 0
        for num in numbers:
            if key is None:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1
            if count == 0:
                key = None
        return key
