"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        all_path = []

        def find_path_core(root, path=[], crurrent_sum=0):
            crurrent_sum += root.val
            path.append(root)
            if crurrent_sum == target and root.left is None and root.right is None:
                all_path.append([node.val for node in path])
            if root.left:
                find_path_core(root.left, path, crurrent_sum)
            if root.right:
                find_path_core(root.right, path, crurrent_sum)
            path.pop()

        find_path_core(root)
        return all_path
