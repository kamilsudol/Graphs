from .graphic_sequence import load_sequence, is_graphic_sequence
from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle_colormap

import numpy as np
import random as rnd

# just for tests
# from lib.Project_1.random_graph import random_graph_edges


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
        result[comp[i] - 1].append(i+1)
    return result


def components_recursive(nr, v, graph, comp):
    for u in graph[v]:
        if comp[u-1] == -1:
            comp[u-1] = nr
            components_recursive(nr, u-1, graph, comp)


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


def create_colormap(list):
    colormap = {}
    for row in list:
        random_color = (rnd.random(), rnd.random(), rnd.random())
        for x in row:
            colormap[x] = random_color
    return colormap


def find_largest_connected_component(): #4 2 2 3 2 1 4 2 2 2 2
    seq = load_sequence()
    result = is_graphic_sequence(seq)
    if result is not False:
        print("Ciag jest graficzny")
        graph = adjacency_matrix_to_list(result)
        g = create_igraph_from_adjacency_matrix(result)
        connected_components_list = components(graph)
        largest(connected_components_list)
        colormap = create_colormap(connected_components_list)
        plot_igraph_on_circle_colormap(g, colormap)
    else:
        print("Ciag nie jest graficzny")

    ''' test
    graph = random_graph_edges(25, 30)
    g = create_igraph_from_adjacency_matrix(graph)
    test = adjacency_matrix_to_list(graph)
    connected_components_list = components(test)
    largest(connected_components_list)
    colormap = create_colormap(connected_components_list)
    plot_igraph_on_circle_colormap(g, colormap)
    # print(colormap[1])
    # print(connected_components_list)
    '''