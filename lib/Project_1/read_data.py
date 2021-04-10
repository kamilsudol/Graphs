import re
from .MatrixRepresentation import *


def check_adjacency(matrix):
    for i in range(len(matrix)):
        for j in range(int(i / 2)):
            if int(matrix[i][j]) != int(matrix[j][i]):
                return False
        if int(matrix[i][i]) != 0:
            return False
    return True


def check_columns(matrix):
    flag = 2 * len(matrix[0])
    check_flag = 0
    for row in matrix:
        for x in row:
            check_flag += int(x)
    return flag == check_flag


def check_redundant(matrix):
    unique_columns = np.unique(np.array(matrix), axis=1)
    return len(unique_columns) == len(matrix)


def resolve_matrix_type(matrix):
    if len(matrix) == len(matrix[0]):
        if check_adjacency(matrix):
            if check_columns(matrix) and check_redundant(matrix):
                return MatrixRepresentation.UndeterminedMatrix
            return MatrixRepresentation.AdjacencyMatrix
        elif check_columns(matrix) and check_redundant(matrix):
            return MatrixRepresentation.IncidenceMatrix
    else:
        if check_columns(matrix) and check_redundant(matrix):
            return MatrixRepresentation.IncidenceMatrix

    print("Wrong input!")
    SystemExit(1)


def load_list(filename):
    matrix = []
    
    with open(filename, 'r') as file:
        for x in file:
            matrix.append(list(map(int, filter(None, re.split(' |\n', x.split(".")[1])))))

    return matrix


def load_matrix(filename):
    matrix = []
    
    with open(filename, 'r') as file:
        for x in file:
            matrix.append(list(map(int, filter(None, re.split('\n| ', x)))))

    return matrix


def read_matrix_from_file(name):  # funkcja zwraca liste zawierajaca macierz wraz z jej typem
    try:
        return [load_list(name), MatrixRepresentation.List]
    except IndexError:
        m = load_matrix(name)
        return [m, resolve_matrix_type(m)]
