class Solution:
    obj = None

    # @return: The same instance of this class every time

    @classmethod
    def getInstance(cls):
        # write your code here
        if not Solution.obj:
            Solution.obj = cls()
        return Solution.obj
