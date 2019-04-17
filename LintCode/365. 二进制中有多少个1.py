class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        count = 0
        if num < 0:
            num = num & 0xffffffff
        while num:
            count += 1
            num = (num - 1) & num
        return count
