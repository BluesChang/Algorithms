'''
题目：输入两个树结点，求它们的最低公共祖先。
'''


class Solution:
    def get_last_common_parent(self, root, node1, node2):
        if root is None:
            return None
        if root == node1 or root == node2:
            return root
        left_result = self.get_last_common_parent(root.left, node1, node2)
        right_result = self.get_last_common_parent(root.right, node1, node2)
        # A 和 B 一边一个
        if left_result and right_result:
            return root
        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result
        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result
        # 左右子树都没有
        return None
