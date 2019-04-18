class Solution:
    """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """

    def numbersByRecursion(self, n):
        # write your code here
        top = pow(10, n)
        result = []
        for i in range(1, top):
            result.append(i)
        return result
