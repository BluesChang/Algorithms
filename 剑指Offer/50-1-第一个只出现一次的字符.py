'''
题目：在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，则输出‘b’。
'''


class Solution:
    def first_not_repeating_char(self, string):
        count = {}
        for i in string:
            count[i] = count.get(i, 0) + 1
        for i in string:
            if count[i] == 1:
                return i
