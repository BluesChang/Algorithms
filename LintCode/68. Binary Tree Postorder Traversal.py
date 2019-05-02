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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        self.result = []
        self.postorder_traversal(root)
        return self.result

    def postorder_traversal(self, root):
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        self.result.append(root.val)
