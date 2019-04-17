"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """

    def buildTree(self, inorder, preorder):
        # write your code here
        if not preorder or not inorder:
            return  #

        root = TreeNode(inorder[0])
        index = preorder.index(inorder[0])

        root.left = self.buildTree(inorder[1:index + 1], preorder[:index])
        root.right = self.buildTree(inorder[index + 1:], preorder[index + 1:])

        return root
