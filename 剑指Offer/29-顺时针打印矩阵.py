'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''


class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """

    def print_matrix_clock_wisely(self, matrix):
        # write your code here
        if not matrix:
            return
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while cols > start * 2 and rows > start * 2:
            self.print_matrix_in_circle(matrix, rows, cols, start)
            start += 1

    def print_matrix_in_circle(self, matrix, rows, cols, start):
        end_col = cols - start - 1
        end_row = rows - start - 1

        for i in range(start, end_col + 1):
            print(matrix[start][i])

        if start < end_row:
            for i in range(start + 1, end_row + 1):
                print(matrix[i][end_col])

        if start < end_col and start < end_row:
            for i in reversed(range(start, end_col)):
                print(matrix[end_row][i])

        if start < end_row - 1 and start < end_col:
            for i in reversed(range(start + 1, end_row)):
                print(matrix[i][start])


Solution().print_matrix_clock_wisely([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
