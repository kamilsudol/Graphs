def print_int_matrix(matrix):
    for row in matrix:
        print('[ ', end='')
        for val in row:
            print('{:<2d} '.format(int(val)), end='')
        print(']')
