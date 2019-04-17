class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        result = [1, 1]

        if n == 0:
            return 0

        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])

        return result[n]
