class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    def replaceBlank(self, string, length):
        # write your code here
        if length == 0:
            return 0
        blank_count = 0
        for s in string:
            if s == ' ':
                blank_count += 1
        new_length = length + blank_count * 2
        p1 = length - 1
        p2 = new_length - 1
        while p1 >= 0:
            if string[p1] != ' ':
                string[p2] = string[p1]
                p1 -= 1
                p2 -= 1
            else:
                string[p2 - 2] = '%'
                string[p2 - 1] = '2'
                string[p2] = '0'
                p1 -= 1
                p2 -= 3
        return new_length
