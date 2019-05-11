'''
题目：请实现一个函数，用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符“go”时，第一个只出现一次的字符是‘g'：
当从该字符流中读出前6个字符“google”，第一个只出现一次的字符是’l'。
'''

import sys


class Solution:
    def __init__(self):
        self.orrcurrence = [-1 for i in range(256)]

    def insert(self, ch):
        if self.orrcurrence[ord(ch)] == -1:
            self.orrcurrence[ord(ch)] = self.index
        elif self.orrcurrence[ord(ch)] >= 0:
            self.orrcurrence[ord(ch)] = -2
        self.index += 1

    def first_appearing_once(self):
        min_index = sys.maxsize
        for i in range(256):
            if 0 <= self.orrcurrence[i] < min_index:
                ch = chr(i)
                min_index = self.orrcurrence[i]
        return ch
