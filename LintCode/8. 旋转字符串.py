class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, s, offset):
        # write your code here
        if len(s) > 0:
            offset %= len(s)
        tmp = (s + s)[len(s) - offset:len(s) * 2 - offset]
        for i in range(len(tmp)):
            s[i] = tmp[i]
