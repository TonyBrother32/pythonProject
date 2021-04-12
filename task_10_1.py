class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(str, self.matrix)).replace(",", " ").replace("[", " ").replace("]", " ")

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_sum.append(row)
        return "\n".join(map(str, matrix_sum)).replace(",", " ").replace("[", " ").replace("]", " ")


matrix1 = Matrix([[10, 5, 8], [13, 4, 9], [17, 9, 1]])
matrix2 = Matrix([[3, 9, 7], [5, 7, 4], [1, 9, 5]])
print(f'Матрица \n{matrix1}')
print(f'Матрица \n{matrix2}')
print(f'Сумма матриц \n{matrix1 + matrix2}')
