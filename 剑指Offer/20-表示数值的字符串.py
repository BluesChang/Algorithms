'''
题目:
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''


class Solution:
    def is_numeric(self, str):
        if not str or len(str) <= 0:
            return False
        str_list = [i.lower() for i in str]
        if 'e' in str_list:
            e_index = str_list.index('e')
            front = str_list[:e_index]
            behind = str_list[e_index + 1:]
            if '.' in behind or behind == 0:
                return False
            is_front = self.is_digit(front)
            is_behind = self.is_digit(behind)
            if is_front is False or is_behind is False:
                return False
        else:
            is_num = self.is_digit(str_list)
            return is_num
        return True

    def is_digit(self, str_list):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        dot_count = 0
        for i in range(len(str_list)):
            if str_list[i] not in num:
                return False
            if str_list[i] == '.':
                dot_count += 1
            if str_list[i] in '+-' and i != 0:
                return False
        if dot_count > 1:
            return False
        return True


class Solution2:
    def is_numeric(self, str):
        try:
            return float(str)
        except:
            return False


class Solution3:
    def is_numeric(self, str):
        if not str:
            return 0
        import re
        return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]*)?$', str)


print(Solution().is_numeric('-1E-16'))
print(Solution().is_numeric('1a3.14'))
print('-----------------------------')
print(Solution2().is_numeric('-1E-16'))
print(Solution2().is_numeric('1a3.14'))
print('-----------------------------')
print(Solution3().is_numeric('-1E-16'))
print(Solution3().is_numeric('1a3.14'))
