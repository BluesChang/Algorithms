class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        assert (n >= 0 and 0 <= k <= 9)
        count = 0
        for i in range(n + 1):
            count += str(i).count(str(k))
        return count
