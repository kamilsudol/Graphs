import random as rng

from lib.Project_1.matrix_conversions import adjacency_matrix_to_incidence_matrix
from lib.Project_1.igraph_creation import create_igraph_from_incidence_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from lib.Project_1.read_data import print_matrix, print_list, read_matrix_from_file, graph_print
from lib.Project_1.MatrixRepresentation import MatrixRepresentation
from lib.Project_2.retrieve_adj_matrix_from_user import retrieve_adjacency_matrix_from_user
from lib.Project_2.is_duplicate_edge import is_duplicate_edge



# Pick two random edges from incidence matrix
# inc -> graph as incidence matrix
# num_vertices -> number of vertices in a graph (number of rows)
# num_edges -> number of edges in a graph
# Returns array of data in order edge one column, edge two column, edge one vertices, edge two vertices
def roll_edges(inc, num_vertices, num_edges):
    rng.seed()

    edge_one_col = -1
    edge_two_col = -1
    edge_one_vertices = [-1, -1]
    edge_two_vertices = [-1, -1]

    # Pick two different edges
    while edge_one_col == edge_two_col or edge_one_vertices[0] == edge_two_vertices[1] or edge_one_vertices[1] == edge_two_vertices[0]:
        edge_one_col = rng.randint(0, num_edges)
        edge_two_col = rng.randint(0, num_edges)

        edge_one_vertices = find_vertices(num_vertices, inc, edge_one_col)
        edge_two_vertices = find_vertices(num_vertices, inc, edge_two_col)

    return [edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices]

# Swaps vertex to another edge
# row -> row index of vertex to be swapped
# col1 -> column index of edge one 
# col2 -> column index of edge two
# matrix -> graph as incidence matrix
def swap_between_columns(row, col1, col2, matrix):
    temp = matrix[row][col1]
    matrix[row][col1] = matrix[row][col2]
    matrix[row][col2] = temp

# Finds vertices in an edge
# num_vertices -> number of vertices (number of rows)
# inc_matrix -> graph as incidence matrix
# edge_index -> column index of an edge
# Returns indices of vertices in an edge as an array [v1, v2] 
def find_vertices(num_vertices, inc_matrix, edge_index):
    vertices = [-1, -1]
    for row in range(num_vertices):
        # If cell in column is a vertex
        if inc_matrix[row][edge_index] == 1:
            # and haven't found vertex one
            if vertices[0] == -1:
                # Save vertex one
                vertices[0] = row
            else:
                # Save vertex two
                vertices[1] = row
    return vertices

# Perform up to a given number of edge swaps
# on a graph by swapping vertices between edges
# adj-> graph as adjacency matrix
# num_shuffles -> number of vertex shuffles to be executed
# guard_limit -> maximum number of failed swap attempts
# plots -> True/False: will it plot the graph previous to randomization
# Returns a list [inc, shuffles_done, is_fully_randomized]
# inc -> the modified incidence matrix
# shuffles_done -> number of executed edge swaps
# is_fully_randomized -> True/False: has it performed the given amount of swaps
def randomize_edges(adj, num_shuffles, guard_limit=200, plots=False):

    inc = adjacency_matrix_to_incidence_matrix(adj)
    if plots:
        graph = create_igraph_from_incidence_matrix(inc)
        plot_igraph_on_circle(graph)
    num_vertices = len(inc)
    num_edges = len(inc[0]) - 1

    shuffles_done = 0
    guard = 0
    while shuffles_done < num_shuffles:
        edge_one_col, edge_two_col, edge_one_vertices, edge_two_vertices = roll_edges(inc, num_vertices, num_edges)

        # If vertex one in edges one and two is the same vertex
        if  edge_one_vertices[0] == edge_two_vertices[0] \
            or edge_one_vertices[1] == edge_two_vertices[1] \
            or edge_one_vertices[1] == edge_two_vertices[0] \
            or edge_one_vertices[0] == edge_two_vertices[1] \
            or is_duplicate_edge(inc, edge_one_vertices[0], edge_two_vertices[1], edge_two_col) \
            or is_duplicate_edge(inc, edge_two_vertices[0], edge_one_vertices[1], edge_one_col):

            guard += 1
            if guard > guard_limit:
                return [inc, shuffles_done, False]
            else:
                continue
        else:
            # Swap first vertex
            swap_between_columns(edge_one_vertices[0], edge_one_col, edge_two_col, inc)
            swap_between_columns(edge_two_vertices[0], edge_one_col, edge_two_col, inc)
            shuffles_done += 1

    return [inc, shuffles_done, True]

def test_randomization(filename=None, output_format=None, num_shuffles=None, plots=None):
    if filename == None:
        adj = retrieve_adjacency_matrix_from_user()
    else:
        matrix, rep = read_matrix_from_file(filename)
        adj = rep.convert_func(MatrixRepresentation.AdjacencyMatrix)(matrix)
    
    if num_shuffles == None:
        num_shuffles = int(input("Podaj liczbe randomizacji.\n"))

    if plots == None or plots == 'y':
        plots = True
    elif plots == 'n':
        plots = False

    representation = MatrixRepresentation.IncidenceMatrix

    start_incidence = adjacency_matrix_to_incidence_matrix(adj)
    print("Przed randomizacja:")
    graph_print(representation, start_incidence, output_format)
    graph = create_igraph_from_incidence_matrix(start_incidence)
    if plots: plot_igraph_on_circle(graph)

    [randomized_incidence, shuffles_done, is_fully_randomized] = randomize_edges(adj, num_shuffles, False)
    print(f"Po randomizacji {shuffles_done} razy:")
    graph_print(representation, randomized_incidence, output_format)
    graph = create_igraph_from_incidence_matrix(randomized_incidence)
    if plots: plot_igraph_on_circle(graph)
