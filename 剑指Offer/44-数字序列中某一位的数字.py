'''
题目：数字以0123456789101112131415……的格式序列化到一个字符串序列中。在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
'''


class Solution:
    def digit_at_index(self, index):
        if index < 0:
            return None
        digits = 1
        while True:
            numbers = 10 if digits == 1 else 9 * 10 ** (digits - 1)
            if index < numbers * digits:
                number = (0 if digits == 1 else 10 ** (digits - 1)) + index / digits
                index_from_right = digits - index % digits
                for i in range(1, index_from_right):
                    number /= 10
                return int(number % 10)
            index -= digits * numbers
            digits += 1
        return None


print(Solution().digit_at_index(1))
