'''
题目：请完成一个函数，输入一颗二叉树，该函数输出它的镜像。
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
