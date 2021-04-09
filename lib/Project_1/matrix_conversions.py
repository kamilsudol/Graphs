import numpy as np


def incidence_matrix_to_list(matrix):
    converted_matrix = [[] for i in range(len(matrix))]
    tmp_matrix = np.array(matrix, dtype=int).transpose()
    for row in tmp_matrix:
        first_flag = False
        first_idx = 0
        second_idx = 0
        tmp_idx = 0
        for x in row:
            if x == 1 and first_flag is False:
                first_flag = True
                first_idx = tmp_idx
            elif x == 1 and first_flag:
                second_idx = tmp_idx
            tmp_idx += 1
        converted_matrix[first_idx].append(second_idx + 1)
        converted_matrix[second_idx].append(first_idx + 1)
    return converted_matrix


def list_to_incidence_matrix(matrix):
    converted_matrix = []
    tmp_idx = 0
    for row in matrix:
        for x in row:
            new_row = [0 for i in range(len(matrix))]
            new_row[tmp_idx] = 1
            new_row[int(x) - 1] = 1
            converted_matrix.append(new_row)
        tmp_idx += 1
    converted_matrix = np.unique(np.array(converted_matrix).transpose(), axis=1)
    return converted_matrix


def list_to_adjacency_matrix(matrix):
    converted_matrix = np.zeros((len(matrix), len(matrix)), dtype=int)
    tmp_idx = 0
    for row in matrix:
        for x in row:
            converted_matrix[tmp_idx, int(x) - 1] = 1
        tmp_idx += 1
    return converted_matrix


def adjacency_matrix_to_list(matrix):
    converted_matrix = []
    for row in matrix:
        tmp_val = 1
        converted_row = []
        for x in row:
            if int(x):
                converted_row.append(tmp_val)
            tmp_val += 1
        converted_matrix.append(converted_row)
    return converted_matrix


def adjacency_matrix_to_incidence_matrix(matrix):
    return list_to_incidence_matrix(adjacency_matrix_to_list(matrix))


def incidence_matrix_to_adjacency_matrix(matrix):
    return list_to_adjacency_matrix(incidence_matrix_to_list(matrix))