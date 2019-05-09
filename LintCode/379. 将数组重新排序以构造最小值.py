from functools import cmp_to_key


class Solution:
    """
    @param nums: n non-negative integer array
    @return: A string
    """

    def minNumber(self, nums):
        # write your code here
        if not nums:
            return
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'
