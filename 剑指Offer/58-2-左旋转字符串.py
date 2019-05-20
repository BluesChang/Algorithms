'''
题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和
数字2，该函数将返回左旋转2位得到的结果"cdefgab"。
'''

'''
python式方法
'''


class Solution:
    def left_rotate_string(self, s, n):
        if len(s) > 0:
            n %= len(s)
        return (s + s)[n:n + len(s)]


'''
书中方法
'''


class Solution2:
    def reverse(self, data, start, end):
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    def left_rotate_string(self, data, n):
        if not data:
            return
        if len(data) > 0 and n < len(data) and n > 0:
            firstStart = 0
            firstEnd = n - 1
            secondStart = n
            secondEnd = len(data) - 1

            data = list(data)
            self.reverse(data, firstStart, firstEnd)
            self.reverse(data, secondStart, secondEnd)
            self.reverse(data, firstStart, secondEnd)
            return ''.join(data)
