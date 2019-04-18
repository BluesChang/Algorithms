'''
题目：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。不得使用库函数，同时不需要考虑最大数问题。
'''


class Solution:
    g_invalid_input = False

    def power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            g_invalid_input = True
            return 0.0
        if exponent >= 0:
            return self.power_with_exponent(base, exponent)
        else:
            return 1.0 / self.power_with_exponent(base, -exponent)

    def power_with_exponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.power_with_exponent(base, exponent >> 1)
        result *= result
        if exponent & 0x1 == 1:
            result *= base
        return result


print(Solution().power(2, -3), Solution().g_invalid_input)
print(Solution().power(2, 0), Solution().g_invalid_input)
print(Solution().power(-2, 3), Solution().g_invalid_input)
print(Solution().power(0, 1), Solution().g_invalid_input)
print(Solution().power(0, 0), Solution().g_invalid_input)
print(Solution().power(0, -1), Solution().g_invalid_input)
