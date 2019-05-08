'''
题目：输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。例如，输入12，1~12这些整数中包含1的数字有1、10、11和12，1一共出现了5次。
'''
'''
解题思路：
1. 如果第i位（自右至左，从1开始标号）上的数字为0，则第i位可能出现1的次数由更高位决定（若没有高位，视高位为0），等于更高位数字X当前位数的权重10^(i-1)。
2. 如果第i位上的数字为1，则第i位上可能出现1的次数不仅受更高位影响，还受低位影响（若没有低位，视低位为0），等于更高位数字X当前位数的权重10^(i-1)+（低位数字+1）。
3. 如果第i位上的数字大于1，则第i位上可能出现1的次数仅由更高位决定（若没有高位，视高位为0），等于（更高位数字+1）X当前位数的权重10^(i-1)。
'''


class Solution:
    def number_of_1(self, nums):
        base = 1
        count = 0
        while nums // base > 0:
            high, mod = divmod(nums, base * 10)
            current_number, low = divmod(mod, base)
            if current_number > 1:
                count += high * base + base
            elif current_number == 1:
                count += high * base + low + 1
            else:
                count += high * base
            base *= 10
        return count
