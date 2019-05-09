'''
题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成“a“，1翻译成”b“，……，……25翻译成”z“。一个数字可能有多少个翻译。例如，12258有5种
不同的翻译，分别是“bccfi”、“bwfi”、“bczi“、”mcfi“和”mzi“。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
'''


class Solution:
    def get_translation_count(self, numbers):
        if not numbers:
            return
        numbers = str(numbers)
        length = len(numbers)
        counts = [0 for i in range(length)]
        for i in reversed(range(length)):
            count = counts[i + 1] if i < length - 1 else 1
            if i < length - 1:
                converted = int(numbers[i]) * 10 + int(numbers[i + 1])
                if 10 <= converted <= 25:
                    count += counts[i + 2] if i < length - 2 else 1
            counts[i] = count
        return counts[0]
