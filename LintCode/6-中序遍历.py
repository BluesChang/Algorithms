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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        self.result=[]
        self.inorder_traversal(root)
        return self.result

    def inorder_traversal(self,root):
        if not root:
            return
        self.inorder_traversal(root.left)
        self.result.append(root.val)
        self.inorder_traversal(root.right)