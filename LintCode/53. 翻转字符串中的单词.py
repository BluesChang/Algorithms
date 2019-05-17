class Solution:
    """
    @param: s: A string
    @return: A string
    """

    def reverseWords(self, s):
        # write your code here
        return ' '.join(reversed(s.strip().split()))
