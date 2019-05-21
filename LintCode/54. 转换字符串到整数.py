import sys


class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def atoi(self, str):
        # write your code here
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
