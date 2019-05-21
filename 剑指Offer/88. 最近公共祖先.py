"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
        if root == A or root == B:
            return root
        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)
        # A 和 B 一边一个
        if left_result and right_result:
            return root
        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result
        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result
        # 左右子树啥都没有
        return None
