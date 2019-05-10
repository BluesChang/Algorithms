'''
题目：在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，则输出‘b’。
'''


class Solution1:
    def first_not_repeating_char(self, string):
        hash_table = [0 for i in range(256)]
        for i in string:
            hash_table[ord(i)] += 1
        for i in string:
            if hash_table[ord(i)] == 1:
                return i


class Solution2:
    def first_not_repeating_char(self, string):
        count = {}
        for i in string:
            count[i] = count.get(i, 0) + 1
        for i in string:
            if count[i] == 1:
                return i
