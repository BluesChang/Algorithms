'''
题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。
'''
'''
Python式方法
'''


class Solution:
    def reverse(self, s):
        # strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))


'''
书中方法
'''


class Solution2:
    def reverse(self, data, start, end):
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    def reverse_sentence(self, data):
        if not data:
            return
        start = 0
        end = len(data) - 1
        data = list(data)
        self.reverse(data, start, end)
        start = end = 0
        while end < len(data):
            if data[start] == ' ':
                start += 1
                end += 1
            elif data[end] == ' ':
                end -= 1
                self.reverse(data, start, end)
                end += 1
                start = end
            elif end == len(data) - 1:
                self.reverse(data, start, end)
                break
            else:
                end += 1
        return ''.join(data)
