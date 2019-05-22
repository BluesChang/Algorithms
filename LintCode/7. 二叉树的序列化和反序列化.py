"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if not root:
            return ""
        queue = deque([root])
        bfs = []
        while queue:
            node = queue.popleft()
            bfs.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(bfs)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if not data:
            return
        bfs = [TreeNode(int(val)) if val != '#' else None for val in data.split()]
        root = bfs[0]
        nodes = [root]
        root_index = 0
        child_index = 1
        while root_index < len(nodes):
            node = nodes[root_index]
            root_index += 1
            node.left = bfs[child_index]
            node.right = bfs[child_index + 1]
            child_index += 2
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
