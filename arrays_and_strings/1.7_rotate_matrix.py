from helpers.matrix import print_matrix


def rotate_matrix(matrix):
    """
    Given a NxN matrix rotate it 90 degrees to the right
    :param matrix:
    :return:
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # for row in matrix:
    #     row.reverse()

    # This a more suitable for coding interviews approach
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

if __name__ == '__main__':
    matrix = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    print_matrix(matrix)
    rotate_matrix(matrix)
    print_matrix(matrix)