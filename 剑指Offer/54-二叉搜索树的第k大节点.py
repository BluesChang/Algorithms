'''
题目：给定一棵二叉搜索树，请找出其中的第k大的结点。
'''


class Solution:
    def kth_node(self, root, k):
        self.result = []
        self.kth_node_core(root)
        return self.result[k - 1]

    def kth_node_core(self, root):
        if not root:
            return
        self.kth_node_core(root.left)
        self.result.append(root.val)
        self.kth_node_core(root.right)
