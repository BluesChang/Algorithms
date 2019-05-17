class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        # write your code here
        if not A:
            return
        ans = 0
        for num in A:
            ans ^= num
        return ans
