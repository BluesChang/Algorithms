class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        count = {}
        for i in str:
            count[i] = count.get(i, 0) + 1
        for i in str:
            if count[i] == 1:
                return i
