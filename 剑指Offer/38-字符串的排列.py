'''
题目:输入一个字符串，打印出该字符串中字符的所有排列顺序。例如:输入字符串abc，则打印出字符a、b、c所能排列出的所有字符串abc、acb、bac、bca、
cab和cba。
'''


class Solution:
    def permutation(self, str):
        if not str:
            return
        begin = 0
        end = len(str)
        self.permutation_core(str, begin, end)

    def permutation_core(self, str, begin, end):
        if begin >= end:
            print(str)
        else:
            for char in range(begin, end):
                str = list(str)
                print(str)
                str[char], str[begin] = str[begin], str[char]
                str = ''.join(str)
                self.permutation_core(str, begin + 1, end)


print(Solution().permutation('abcd'))
