"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """

    def cloneTree(self, root):
        # write your code here
        if root is None:
            return None
        clone_root = TreeNode(root.val)
        clone_root.left = self.cloneTree(root.left)
        clone_root.right = self.cloneTree(root.right)
        return clone_root
