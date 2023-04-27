"""Заполнение матрицы разными способами"""


def fill_matrix_casual(n: int, m: int) -> list[list]:
    matrix = [[0] * m for i in range(n)]
    filler = 1
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(0, len(row)):
            row[j] = filler
            filler += 1

    return matrix


def fill_matrix_as_snake(n: int, m: int) -> list[list]:
    matrix = [[0] * m for i in range(n)]
    filler = 1
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(0, len(row)):
            if i % 2 == 0:
                row[j] = filler
                filler += 1
            else:
                j += 1
                row[-j] = filler
                filler += 1

    return matrix


if __name__ == '__main__':
    a, b = 5, 5
    print(*fill_matrix_as_snake(a, b), sep='\n')
    print(*fill_matrix_casual(a, b), sep='\n')
