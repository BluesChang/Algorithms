'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。
例如，输入数组{5,7,6,9,11,10,8},则返回true，因为这个整数序列是二叉搜索树的后序遍历结果。如果输入的数组是{7,4,6,5,}，则由于没有哪颗二叉搜索树的
后序遍历结果是这个序列，因此返回false。
'''


class Solution:
    def verify_squence_of_bst(self, sequence):
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1
        for node in sequence[i:-1]:
            if node < root:
                return False
        left = True
        if i > 0:
            left = self.verify_squence_of_bst(sequence[:i])
        right = True
        if i < len(sequence) - 2:
            right = self.verify_squence_of_bst(sequence[i + 1:-1])
        return left and right
