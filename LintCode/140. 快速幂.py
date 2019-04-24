class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b
        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b
        if n % 2 == 1:
            power = (power * a) % b
        return power