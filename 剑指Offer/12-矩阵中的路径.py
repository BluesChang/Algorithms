'''
题目：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含其字符串所有字符的路径。路径可以从矩阵中的任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格，如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3x4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
'''


class Solution:
    def has_path(self, matrix, rows, cols, path):
        if len(matrix) == 0 or rows <= 0 or cols <= 0 or len(path) == 0:
            return False
        visited = [False for i in range(rows * cols)]
        path_length = 0
        for row in range(rows):
            for col in range(cols):
                if self.has_path_core(matrix, rows, cols, row, col, path, path_length, visited):
                    return True
        return False

    def has_path_core(self, matrix, rows, cols, row, col, path, path_length, visited):
        if len(path) == path_length:
            return True
        has_path = False
        if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[path_length] and not \
                visited[row * cols + col]:
            path_length += 1
            visited[row * cols + col] = True
            has_path = self.has_path_core(matrix, rows, cols, row - 1, col, path, path_length, visited) \
                       or self.has_path_core(matrix, rows, cols, row + 1, col, path, path_length, visited) \
                       or self.has_path_core(matrix, rows, cols, row, col - 1, path, path_length, visited) \
                       or self.has_path_core(matrix, rows, cols, row, col + 1, path, path_length, visited)
            if not has_path:
                path_length -= 1
                visited[row * cols + col] = False
        return has_path


class Solution2:
    def has_path(self, matrix, rows, cols, path):
        for row in range(rows):
            for col in range(cols):
                if matrix[row * cols + col] == path[0]:
                    if self.find_path(list(matrix), rows, cols, path[1:], row, col):
                        return True

    def find_path(self, matrix, rows, cols, path, row, col):
        if not path:
            return True
        matrix[row * cols + col] = 0
        if col + 1 < cols and matrix[row * cols + col + 1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], row, col + 1)
        elif col - 1 >= 0 and matrix[row * cols + col - 1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], row, col - 1)
        elif row + 1 < rows and matrix[(row + 1) * cols + col] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], row + 1, col)
        elif row - 1 >= 0 and matrix[(row - 1) * cols + col] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], row - 1, col)
        else:
            return False

matrix = [
    'a', 'b', 't', 'g',
    'c', 'f', 'c', 's',
    'j', 'd', 'e', 'h'
]
print(Solution().has_path(matrix, 3, 4, 'bfce'))
print(Solution2().has_path(matrix, 3, 4, 'bfce'))
