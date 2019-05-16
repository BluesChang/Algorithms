'''
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


class Solution:
    def find_path(self, root, expected_sum):
        if not root:
            return []
        all_path = []

        def find_path_core(root, path=[], crurrent_sum=0):
            crurrent_sum += root.val
            path.append(root)
            if crurrent_sum == expected_sum and root.left is None and root.right is None:
                all_path.append([node.val for node in path])
            if root.left:
                find_path_core(root.left, path, crurrent_sum)
            if root.right:
                find_path_core(root.right, path, crurrent_sum)
            path.pop()

        find_path_core(root)
        return all_path
