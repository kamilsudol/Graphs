import re
import numpy as np
from .MatrixRepresentation import *
from lib.Project_4.DiMatrixRepresentation import DiMatrixRepresentation


def print_list(list):
    i = 1
    for row in list:
        string = str(i) + ". "
        for x in row:
            string += str(x) + " "
        print(string)
        i += 1


def print_matrix(matrix):
    for row in matrix:
        string = ""
        for x in row:
            string += str(x) + " "
        print(string)


def graph_print(matrix_representation_kind, matrix, output_format=None):
    if output_format == None:
        matrix_representation_out = MatrixRepresentation(int(input("Wskaż format wyjściowy macierzy\n - 0 - lista "
                                                               "sąsiedztwa\n - 1 - macierz incydencji\n - 2 - macierz"
                                                               " sąsiedztwa\n> ")))
    else:
        matrix_representation_out = resolve_representation_type_from_input(output_format)

    converted = matrix_representation_kind.convert_func(matrix_representation_out)(matrix)
    if matrix_representation_out == MatrixRepresentation.List:
        print_list(converted)
    else:
        print_matrix(converted)

def check_adjacency(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if int(matrix[i][j]) != int(matrix[j][i]):
                return False
        if int(matrix[i][i]) != 0:
            return False
    return True

def check_digraph_adjacency(matrix):
    for i in range(len(matrix)):
        if int(matrix[i][i]) != 0:
            return False
    return True

def check_columns(matrix):
    tmp_matrix = np.array(matrix, dtype=int).transpose()
    for row in tmp_matrix:
        if sum(row) != 2:
            return False
    return True


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
    raise ValueError

def resolve_representation_type_from_input(output_format):
    if output_format == 'adj':
        return MatrixRepresentation.AdjacencyMatrix
    elif output_format == 'inc':
        return MatrixRepresentation.IncidenceMatrix
    elif output_format == 'list':
        return MatrixRepresentation.List

    print("Wrong input!")
    raise ValueError

def load_list(filename):
    matrix = []
    
    try:
        with open(filename, 'r') as file:
            for x in file:
                matrix.append(list(map(int, filter(None, re.split(' |\n', x.split(".")[1])))))
    except IOError:
        print("Brak pliku o podanej nazwie!")
        raise ValueError

    return matrix


def load_matrix(filename):
    matrix = []
    
    try:
        with open(filename, 'r') as file:
            for x in file:
                matrix.append(list(map(int, filter(None, re.split('\n| ', x)))))
    except ValueError:
        raise ValueError("Adjacency list is not supported in this context")
    except IOError:
        print("Brak pliku o podanej nazwie!")
        raise ValueError

    return matrix


def read_matrix_from_file(name):  # funkcja zwraca liste zawierajaca macierz wraz z jej typem
    try:
        return [load_list(name), MatrixRepresentation.List]
    except IndexError:
        m = load_matrix(name)
        return [m, resolve_matrix_type(m)]
    

def read_digraph_from_file(name):
    m = load_matrix(name)
    if not check_digraph_adjacency(m):
        raise ValueError("Incidence matrix is not supported in this context")

    return [m, DiMatrixRepresentation.AdjacencyMatrix]
