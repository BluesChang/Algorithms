'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
'''


class Solution:
    def find_nums_appear_once(self, data):
        if not data or len(data) < 2:
            return
        result_exclusive_or = 0
        for num in data:
            result_exclusive_or ^= num
        index_of_1 = self.find_first_bit_is_1(result_exclusive_or)
        num1 = num2 = 0
        for i in range(len(data)):
            if self.is_bit_1(data[i], index_of_1):
                num1 ^= data[i]
            else:
                num2 ^= data[i]
        return num1, num2

    def find_first_bit_is_1(self, num):
        index_bit = 0
        while num & 1 == 0:
            num = num >> 1
            index_bit += 1
        return index_bit

    def is_bit_1(self, num, index_bit):
        num = num >> index_bit
        return num & 1


print(Solution().find_nums_appear_once([2, 4, 3, 6, 3, 2, 5, 5]))
