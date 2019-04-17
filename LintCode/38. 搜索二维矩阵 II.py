class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0
        row = 0
        col = len(matrix[0]) - 1
        count = 0
        while row < len(matrix) and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                count += 1
                col -= 1
                row += 1
        return count
