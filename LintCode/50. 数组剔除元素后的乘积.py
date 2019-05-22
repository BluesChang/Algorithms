class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, nums):
        # write your code here
        if not nums:
            return []
        length = len(nums)
        b = [1] * length
        for i in range(1, length):
            b[i] = b[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(length - 2, -1, -1):
            tmp *= nums[i + 1]
            b[i] *= tmp
        return b
