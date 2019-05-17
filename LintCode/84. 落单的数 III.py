class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """

    def singleNumberIII(self, A):
        # write your code here
        if not A or len(A) < 2:
            return
        result_exclusive_or = 0
        for num in A:
            result_exclusive_or ^= num
        index_of_1 = result_exclusive_or & (-result_exclusive_or)
        res = [0, 0]
        for num in A:
            if (num & index_of_1) != 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
