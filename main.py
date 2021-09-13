from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Соблюдайте размерность матрицы")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"задайте другой тип")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Соблюдайте размерность матрицы")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 50], [30, 80],[51, 86] ])
    print(matrix2, '\n')
    print(matrix1 + matrix2, '\n')

    matrix3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, 8]])
    print(matrix1, '\n')

    matrix4 = Matrix([[3, 8, 3], [4, 4, 6], [-8, 4, 8]])
    print(matrix2, '\n')
    print(matrix3 + matrix4)
