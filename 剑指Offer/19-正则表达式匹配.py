'''
题目：
请实现一个函数用来匹配包括’.’和’*’的正则表达式。模式中的字符’.’表示任意一个字符，而’’表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串”aaa”与模式”a.a”和”ab*ac*a”匹配，但是与”aa.a”和”aba”均不匹配
'''


class Solution:
    def match(self, str, pattern):
        if str is None or pattern is None:
            return False
        if len(str) == 0 and len(pattern) == 0:
            return True
        if len(str) != 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if pattern[0] == str[0] or (pattern[0] == '.' and len(str) != 0):
                return self.match(str[1:], pattern[2:]) or self.match(str[1:], pattern) or self.match(str, pattern[2:])
            else:
                return self.match(str, pattern[2:])
        if str[0] == pattern[0] or (pattern[0] == '.' and len(str) > 0):
            return self.match(str[1:], pattern[1:])
        return False


str = "aaa"
pattern = "a.a"
# pattern = "ab*ac*a"
# pattern = "aa.a"
# pattern = "ab*a"
# pattern = ""
print(Solution().match(str, pattern))
