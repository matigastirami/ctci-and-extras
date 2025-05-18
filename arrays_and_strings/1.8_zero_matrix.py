from helpers.matrix import print_matrix


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)


    for row in list(rows):
        for col in range(n):
            matrix[row][col] = 0

    for col in list(cols):
        for row in range(m):
            matrix[row][col] = 0


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 0, 1],
        [6, 7, 8, 5]
    ]
    print_matrix(matrix)
    zero_matrix(matrix)
    print_matrix(matrix)

