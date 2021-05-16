import numpy as np
import random as rnd

from InputArguments import InputArguments

from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from .retrieve_adj_matrix_from_user import retrieve_adjacency_matrix_from_user
from lib.Project_1.read_data import read_matrix_from_file
from lib.Project_1.MatrixRepresentation import MatrixRepresentation


# DFS algorithm
def components(graph):
    nr = 0
    comp = [-1 for x in graph]

    for v in range(len(graph)):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_recursive(nr, v, graph, comp)
    tmp = np.unique(comp)
    result = [[] for x in tmp]
    for i in range(len(comp)):
        result[comp[i] - 1].append(i + 1)
    return result


def components_recursive(nr, v, graph, comp):
    for u in graph[v]:
        if comp[u - 1] == -1:
            comp[u - 1] = nr
            components_recursive(nr, u - 1, graph, comp)


# resolving largest connected components and printing them out
def largest(list):
    max_len = 0
    max_it = 0
    iterator = 1
    for row in list:
        string = "{}) ".format(iterator)
        if len(row) > max_len:
            max_len = len(row)
            max_it = iterator
        for x in row:
            string += str(x) + " "
        print(string)
        iterator += 1
    print("Najwieksza skladowa ma numer {}.".format(max_it))


# creating a dictionary of colors to sign specific connected components on plot
def create_colormap(list):
    colormap = {}
    for row in list:
        random_color = (rnd.random(), rnd.random(), rnd.random())
        for x in row:
            colormap[x] = random_color
    return colormap


def find_largest_connected_component(interactive_input = True):  # 3 3 2 2 2 2 2 2 2
    if interactive_input:
        result = retrieve_adjacency_matrix_from_user()
    else:
        matrix, rep = read_matrix_from_file(InputArguments().args['filename'])
        result = rep.convert_func(MatrixRepresentation.AdjacencyMatrix)(matrix)

    graph = adjacency_matrix_to_list(result)
    g = create_igraph_from_adjacency_matrix(result)
    connected_components_list = components(graph)
    largest(connected_components_list)
    colormap = create_colormap(connected_components_list)
    if interactive_input or InputArguments().args['plots'] == 'y':
        plot_igraph_on_circle(g, colormap)
