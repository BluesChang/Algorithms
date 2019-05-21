'''
题目：请你写一个函数StrToInt，实现把字符串转换成整数这个功能。当然，不能使用atoi或者其他类似的库函数。
'''
import sys


class Solution:
    def str_to_int(self, str):
        str = str.strip()
        if str == "":
            return 0
        i = 0
        sign = 1
        ret = 0
        length = len(str)
        max_int = (1 << 31) - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
        for i in range(i, length):
            if str[i] < '0' or str[i] > '9':
                break
            ret = ret * 10 + int(str[i])
            if ret > sys.maxsize:
                break
        ret *= sign
        if ret >= max_int:
            return max_int
        if ret < max_int * -1:
            return max_int * -1 - 1
        return ret
