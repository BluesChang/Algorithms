'''
题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、4～6和7～8。
'''


class Solution:
    def find_continuous_sequence(self, sum):
        small = 1
        big = 2
        mid = (1 + sum) >> 1
        cur_sum = big + small
        while small < big:
            if cur_sum == sum:
                self.print_continuous_sequence(small, big)
            while cur_sum > sum and small < mid:
                cur_sum -= small
                small += 1
                if cur_sum == sum:
                    self.print_continuous_sequence(small, big)
            big += 1
            cur_sum += big

    def print_continuous_sequence(self, small, big):
        for i in range(small, big + 1):
            print(i)
        print("\n")


Solution().find_continuous_sequence(15)
