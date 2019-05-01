"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        self.result = []
        self.preorder_traversal(root)
        return self.result

    def preorder_traversal(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
