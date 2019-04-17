class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not isinstance(matrix, list):
            return -1
        if not isinstance(target, int):
            return -1
        if len(matrix) != 0:
            row = 0
            col = len(matrix[0]) - 1
            while row < len(matrix) and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
            return False
        else:
            return False
