class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        list1 = [i for i in A]
        list2 = [j for j in B]
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False
