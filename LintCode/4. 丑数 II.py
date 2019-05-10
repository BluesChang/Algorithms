import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        if not n:
            return
        ugly_number = [1] * n
        next_ugly_index = 1
        multiply2 = multiply3 = multiply5 = 0
        while next_ugly_index < n:
            ugly_number[next_ugly_index] = min(ugly_number[multiply2] * 2, ugly_number[multiply3] * 3,
                                               ugly_number[multiply5] * 5)
            while ugly_number[multiply2] * 2 <= ugly_number[next_ugly_index]:
                multiply2 += 1
            while ugly_number[multiply3] * 3 <= ugly_number[next_ugly_index]:
                multiply3 += 1
            while ugly_number[multiply5] * 5 <= ugly_number[next_ugly_index]:
                multiply5 += 1
            next_ugly_index += 1
        return ugly_number[next_ugly_index - 1]
