'''
题目：请实现一个函数，用来判断一颗二叉树是不是对称的，如果一颗二叉树和它的镜像一样，那么它是对称的。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def mirror_recursively(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        node.left, node.right = node.right, node.left
        if node.left is not None:
            self.mirror_recursively(node.left)
        if node.right is not None:
            self.mirror_recursively(node.right)
