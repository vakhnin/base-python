"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List


class Matrix:
    matrix: List[List]

    def __init__(self, matrix: List[List]):
        Matrix.check_matrix(matrix)
        self.matrix = matrix

    def __str__(self):
        max_len = 1
        for row in self.matrix:
            for item in row:
                if len(str(item)) > max_len:
                    max_len = len(str(item))

        result = ''
        for row in self.matrix:
            row_str = ''
            for item in row:
                row_str += str(item).ljust(max_len + 1)
            result += row_str + '\n'
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise NotImplemented
        Matrix.check_matrices_dimensions(self.matrix, other.matrix)
        res_matrix = []
        for y in range(len(self.matrix)):
            row = []
            for x in range(len(self.matrix[y])):
                row.append(self.matrix[y][x] + other.matrix[y][x])
            res_matrix.append(row)
        return Matrix(res_matrix)

    @staticmethod
    def check_matrix(matrix: List[List]):
        row_len = len(matrix[0])
        for row in matrix:
            if row_len != len(row):
                raise ValueError

    @staticmethod
    def check_matrices_dimensions(matrix1: List[List], matrix2: List[List]):
        if len(matrix1) != len(matrix2):
            raise ValueError
        for y in range(len(matrix1)):
            if len(matrix1[y]) != len(matrix2[y]):
                raise ValueError


def main():
    matrix1 = Matrix(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         ]
    )
    print(matrix1)

    matrix2 = Matrix(
        [[5, 6, 7, 8],
         [1, 2, 3, 4],
         [9, 10, 11, 12],
         ]
    )
    print(matrix2)

    print(matrix1 + matrix2)


if __name__ == '__main__':
    main()
