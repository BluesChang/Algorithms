'''
题目：请完成一个函数，输入一颗二叉树，该函数输出它的镜像。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def mirror_recursively(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        root.left, root.right = root.right, root.left
        if root.left is not None:
            self.mirror_recursively(root.left)
        if root.right is not None:
            self.mirror_recursively(root.right)
