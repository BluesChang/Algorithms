# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
方法一：需要重复遍历节点多次的解法
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        diff = self.tree_depth(root.left) - self.tree_depth(root.right)
        if diff > 1 or diff < -1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def tree_depth(self, root):
        if not root:
            return 0
        return max(self.tree_depth(root.left), self.tree_depth(root.right)) + 1


'''
方法二：每个节点只遍历一遍
'''


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        depth = [0]
        return self.is_balanced_core(root, depth)

    def is_balanced_core(self, root, depth):
        if not root:
            depth[0] = 0
            return True
        left = [0]
        right = [0]
        if self.is_balanced_core(root.left, left) and self.is_balanced_core(root.right, right):
            diff = left[0] - right[0]
            if -1 <= diff <= 1:
                depth[0] = 1 + max(left[0], right[0])
                return True
        return False
