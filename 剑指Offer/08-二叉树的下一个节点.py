'''
题目：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，
同时包含指向父结点的指针。
'''
'''
思路：
（1） 若该节点存在右子树：则下一个节点为右子树最左子节点
（2） 若该节点不存在右子树：这时分两种情况：
 2.1 该节点为父节点的左子节点，则下一个节点为其父节点
 2.2 该节点为父节点的右子节点，则沿着父节点向上遍历，直到找到一个节点的父节点的左子节点为该节点，
 则该节点的父节点为下一个节点（如图节点I，沿着父节点一直向上查找找到B（B为其父节点的左子节点），
 则B的父节点A为下一个节点）。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


def next_node(pNode):
    if not pNode:
        return None
    if pNode.right is not None:
        pNode = pNode.right
        while pNode.left is not None:
            pNode = pNode.left
        return pNode
    elif pNode.parent is not None:
        while pNode.parent is not None and pNode.parent.right == pNode:
            pNode = pNode.parent
        return pNode.parent

