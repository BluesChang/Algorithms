'''
题目：请实现一个函数，用来判断一颗二叉树是不是对称的，如果一颗二叉树和它的镜像一样，那么它是对称的。
'''


class Solution:
    def is_symmetrical(self, root):
        return self.is_symmetrical(root)

    def symmetrical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.symmetrical(root1.left, root2.right) and self.symmetrical(root1.right, root2.left)
