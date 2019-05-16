'''
题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


class Solution:
    def tree_depth(self, root):
        if not root:
            return 0
        return max(self.tree_depth(root.left), self.tree_depth(root.right)) + 1
