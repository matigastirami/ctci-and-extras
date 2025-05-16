def print_matrix(matrix):
    if not matrix:
        print('No matrix given')
        return

    n = len(matrix)
    for i in range(n):
        print(matrix[i])