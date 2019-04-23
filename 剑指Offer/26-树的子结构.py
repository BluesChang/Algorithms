'''
题目：输入两颗二叉树A和B，判断B是不是A的子结构。
       1                3
      / \              /
A = 2   3      B =  4
        /
       4
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """

    def has_subtree(self, T1, T2):
        # write your code here
        result = False
        if T1 is not None and T2 is not None:
            if self.equal(T1.val, T2.val):
                result = self.does_tree1_have_tree2(T1, T2)
            if not result:
                result = self.has_subtree(T1.left, T2)
            if not result:
                result = self.has_subtree(T1.right, T2)
        return result

    def does_tree1_have_tree2(self, T1, T2):
        if T2 is None:
            return True
        if T1 is None:
            return False
        if not self.equal(T1.val, T2.val):
            return False
        return self.does_tree1_have_tree2(T1.left, T2.left) and self.does_tree1_have_tree2(T1.right, T2.right)

    def equal(self, num1, num2):
        if num1 - num2 > -0.0000001 and num1 - num2 < 0.0000001:
            return True
        else:
            return False
