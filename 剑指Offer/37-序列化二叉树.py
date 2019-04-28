'''
题目：请实现两个函数，分别用来序列化和反序列化二叉树。
'''


class Solution:
    def serialize(self, root):
        if not root:
            print('$,', end='')
            return
        print(root.val, end='')
        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self, serialize):
        if serialize:
            serialize = iter(serialize.split(','))

        def spanning_tree():
            data = next(serialize)
            if data == '$':
                return None
            node = TreeNode(data)
            node.left = spanning_tree()
            node.right = spanning_tree()
            return node

        return spanning_tree()
