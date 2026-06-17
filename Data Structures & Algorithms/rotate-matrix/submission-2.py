class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Approach 1: Brute Force

        # rows = len(matrix)
        # cols = len(matrix[0])
        # new_matrix = [[0] * cols for _ in range(rows)]

        # for i in range(rows):
        #     for j in range(cols):
        #         new_matrix[j][rows - 1 - i] = matrix[i][j]

        # for i in range(rows):
        #     for j in range(cols):
        #         matrix[i][j] = new_matrix[i][j]


        # Approach 2: Rotate By Four Cells

        # n = len(matrix)
        # l = 0
        # r = n - 1

        # while l < r:
        #     for i in range(r - l):
        #         top, bottom = l, r

        #         tmp = matrix[top][l + i]
        #         matrix[top][l + i] = matrix[bottom - i][l]
        #         matrix[bottom - i][l] = matrix[bottom][r - i]
        #         matrix[bottom][r - i] = matrix[top + i][r]
        #         matrix[top + i][r] = tmp

        #     r -= 1
        #     l += 1


        # Approach 3: Reverse And Transpose

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]