class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """

    def spiralOrder(self, matrix):
        # write your code here
        result = []
        if not matrix:
            return result
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while cols > start * 2 and rows > start * 2:
            result = self.print_matrix_in_circle(matrix, rows, cols, start, result)
            start += 1
        return result

    def print_matrix_in_circle(self, matrix, rows, cols, start, result):
        end_col = cols - start - 1
        end_row = rows - start - 1

        for i in range(start, end_col + 1):
            result.append(matrix[start][i])

        if start < end_row:
            for i in range(start + 1, end_row + 1):
                result.append(matrix[i][end_col])

        if start < end_col and start < end_row:
            for i in reversed(range(start, end_col)):
                result.append(matrix[end_row][i])

        if start < end_row - 1 and start < end_col:
            for i in reversed(range(start + 1, end_row)):
                result.append(matrix[i][start])
        return result
