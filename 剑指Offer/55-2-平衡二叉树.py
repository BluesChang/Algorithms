'''
题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
'''
'''
方法一：需要重复遍历节点多次的解法
'''


class Solution1:
    def is_balanced(self, root):
        if root is None:
            return True
        diff = self.tree_depth(root.left) - self.tree_depth(root.right)
        if diff > 1 or diff < -1:
            return False
        return self.is_balanced(root.left) and self.is_balanced(root.right)

    def tree_depth(self, root):
        if not root:
            return 0
        return max(self.tree_depth(root.left), self.tree_depth(root.right)) + 1


'''
方法二：每个节点只遍历一遍
'''


class Solution2:
    def is_balanced(self, root):
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

