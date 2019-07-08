# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
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
