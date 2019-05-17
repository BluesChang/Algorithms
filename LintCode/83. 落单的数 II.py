class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumberII(self, A):
        # write your code here
        if not A:
            return
        bit_sum = [0] * 32
        for num in A:
            for i in range(32):
                if ((1 << i) & num) != 0:
                    bit_sum[i] += 1
        res = 0
        for i in range(32):
            if (bit_sum[i] % 3) == 1:
                res += 1 << i
        return res
