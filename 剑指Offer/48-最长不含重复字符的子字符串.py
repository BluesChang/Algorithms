'''
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含‘a’~‘z’的字符。例如，在字符串”arabcacfr“中，
最长的不含重复字符的子字符串是“acfr”，长度为4。
'''


class Solution:
    def longest_substring_without_duplication(self, str):
        if not str:
            return
        string = list(str)
        current_length = 0
        max_length = 0
        position = [0] * 26
        for i in range(len(string)):
            prev_index = position[ord(string[i]) - ord('a')]
            if prev_index < 0 or i - prev_index > current_length:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                current_length = i - prev_index
            position[ord(string[i]) - ord('a')] = i
        if current_length > max_length:
            max_length = current_length
        return max_length


print(Solution().longest_substring_without_duplication('arabcacfr'))
