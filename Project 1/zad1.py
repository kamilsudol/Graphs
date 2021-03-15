import math
import matplotlib.pyplot as plt
import re
from igraph import *
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


def conversion(input):
    if input[1] == 0:
        list_to_adjacency_matrix(input[0])
        # list_to_incidence_matrix(matrix)


def check_adjacency(matrix):
    for i in range(len(matrix)):
        for j in range(int(i/2)):
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


def file_reader(name): #funkcja zwraca liste zawierajaca macierz wraz z jej typem, gdzie 0 - lista sasiedztwa, 1 - macierz incydencji, 2 - macierz sasiedztwa, 3 - oba
    matrix = []
    try:
        file = open(name, 'r')
        for x in file:
            matrix.append(list(filter(None, re.split(' |\n', x.split(".")[1]))))
        file.close()
        return [matrix, 0]
    except IndexError:
        file = open(name, 'r')
        for x in file:
            matrix.append(list(filter(None, re.split('\n| ', x))))
        file.close()
        return [matrix, resolve_type(matrix)]


def resolve_type(matrix):
    if len(matrix) == len(matrix[0]):
        if check_adjacency(matrix):
            if check_columns(matrix) and check_redundant(matrix):
                return 3
            return 2
        elif check_columns(matrix) and check_redundant(matrix):
            return 1
    else:
        if check_columns(matrix) and check_redundant(matrix):
            return 1
    print("Wrong input!")
    SystemExit(1)


def load_row():
    row = input().split()
    row = list(map(int, row))
    return row


def load_matrix():
    matrix = []
    row = load_row()

    while len(row):
        matrix.append(row)
        row = load_row()

    return matrix


# assume simple graph (matrix symmetric with respect to the diagonal and only zeros on diagonal)
# use upper right part
def create_igraph_from_adjacency_matrix(matrix):
    g = Graph()
    g.add_vertices(len(matrix))
    skip_diagonal = 1

    for row_num, row in enumerate(matrix):
        for col_num, val in enumerate(row[row_num + skip_diagonal:]):
            if val == 1:
                g.add_edges([(row_num, col_num + row_num + skip_diagonal)])

    return g


# assume simple graph (there is no -1 in the matrix and sum of numbers in a column is 2)
def create_igraph_from_incidence_matrix(matrix):
    g = Graph()
    g.add_vertices(len(matrix))

    if len(matrix) == 0:
        raise Exception()

    for col_num in range(len(matrix[0])):
        edge_vertices = []

        for row_num in range(len(matrix)):
            if matrix[row_num][col_num] == 1:
                edge_vertices.append(row_num)

        if len(edge_vertices) == 2:
            g.add_edges([edge_vertices])

    return g


# output fits inside [0, 1] x [0, 1] square
def span_vertices_on_circle(num_of_vertices):
    scaling_factor = 0.5  # bigger => more space outside main, invisible circle and boundaries of region

    vertices = []
    for i in range(num_of_vertices):
        num_of_vertices_clockwise = num_of_vertices - i
        first_vertex_at_the_top_offset = math.pi / 2
        fraction_of_angle = 2 * math.pi / num_of_vertices * num_of_vertices_clockwise + first_vertex_at_the_top_offset
        vertices.append([math.cos(fraction_of_angle) / (2 + scaling_factor) + 0.5,
                         math.sin(fraction_of_angle) / (2 + scaling_factor) + 0.5])

    return vertices


def plot_vertices(vertices, ax):
    circle_radius = 0.04  # 4% of plot width. Maybe make it function of len(vertices)?
    label_from_1 = 1

    for i in range(len(vertices)):
        vertex = plt.Circle((vertices[i][0], vertices[i][1]), circle_radius, color='r', zorder=10)
        ax.add_patch(vertex)
        plt.text(vertices[i][0], vertices[i][1], str(i + label_from_1), ha='center', va='center', fontsize='medium',
                 zorder=11)


def plot_edges(vertices, es):
    for edge in es:
        plt.plot([vertices[edge.source][0], vertices[edge.target][0]],
                 [vertices[edge.source][1], vertices[edge.target][1]])


def normalize_plot(ax):
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    ax.set_aspect('equal')


def plot_igraph_on_circle(g):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(g.vcount())
    plot_vertices(vertices, ax)
    plot_edges(vertices, g.es)

    normalize_plot(ax)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # m = load_matrix()
    # g = create_igraph_from_adjacency_matrix(m)
    # # g = create_igraph_from_incidence_matrix(m)
    # plot_igraph_on_circle(g)
    # file_reader("m_incydencji.txt")
    matrix_obj = file_reader("l_sasiedztwa.txt")
    # converted = list_to_adjacency_matrix(matrix_obj[0])
    # adjacency_matrix_to_list(converted)
    converted = list_to_incidence_matrix(matrix_obj[0])
    incidence_matrix_to_list(converted)
    # g = create_igraph_from_incidence_matrix(converted)
    # plot_igraph_on_circle(g)
    # file_reader("m_sasiedztwa.txt")
