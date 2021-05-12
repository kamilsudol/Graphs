from math import floor
from lib.Project_2.largest_connected_component import components
from lib.Project_2.graphic_sequence import is_graphic_sequence
from lib.Project_1.MatrixRepresentation import MatrixRepresentation
from lib.Project_1.read_data import graph_print, read_matrix_from_file
import lib.Project_1.matrix_conversions as matconv
import lib.Project_1.random_graph as rngraph
import lib.Project_1.igraph_creation as icreate
import lib.Project_1.plot_igraph_on_circle as plot
import lib.Project_2.edge_randomizer as edrng
import lib.Project_2.largest_connected_component as largcomp
import random as rng

# Check if the incidence matrix already contains an edge
# inc -> incidence matrix
# v_one -> row index of vertex one in checked edge
# v_two -> row index of vertex two in checked edge
# checked_edge -> column index of the checked edge
# Returns True if there is a duplicate, False otherwise
def is_duplicate_edge(inc, v_one, v_two, checked_edge):
    # Get row indexes of vertices in checked edge
    for edge in range(len(inc[v_one])):
        if edge != checked_edge:
            #  Get row indexes of vertices in current edge
            [vertex_one_temp, vertex_two_temp] = edrng.find_vertices(len(inc), inc, edge)

            # Check if the vertices in current edge are the same as those in checked edge
            if v_one == vertex_one_temp and v_two == vertex_two_temp:
                return True
    return False

# Get graphic sequence from incidence matrix
# inc -> incidence matrix
# num_vertices -> number of vertices in the incidence matrix(number of rows)
# Returns graphic sequence as list
def calculate_graphic_seq_from_incidence(inc, num_vertices):
    graphic_seq = []
    vertex_degree = 0

    for row in range(num_vertices):
        # Calculate the degree of a single vertex by adding all edges that it belongs to
        for vertex in inc[row]:
            vertex_degree += vertex
        graphic_seq.append(vertex_degree)
        vertex_degree = 0
    
    return graphic_seq

#DEPRECATED
# Rewire edge by changing to which vertices it connects
# inc -> incidence matrix
# v_one -> row index of vertex one in incidence matrix
# v_two -> row index of vertex two in incidence matrix
# Returns modified incidence matrix
def rewire_edge(inc, v_one, v_two):
    v_one_deg = 0
    v_two_deg = 0

    # Get degree of vertex one and two by adding the edges they belong to
    for edge in range(len(inc[v_one])):
        v_one_deg += inc[v_one][edge]
        v_two_deg += inc[v_two][edge]

    # If degree of vertex one is bigger than degree of vertex two and for each edge in incidence matrix
    if v_one_deg > v_two_deg:
        for edge in range(len(inc[v_one])):
            # If the edge connects to vertex one and doesn't connect to vertex two and edge between one and two doesn't exist
            if inc[v_one][edge] == 1 and inc[v_two][edge] == 0 and not is_duplicate_edge(inc, v_one, v_two, edge):
                # Disconnect edge from vertex one
                inc[v_one][edge] = 0
                # Connect the edge to vertex two
                inc[v_two][edge] = 1
                break
    # If degree of vertex two is bigger or equal than degree of vertex one and for each edge in incidence matrix
    else:
        for edge in range(len(inc[v_two])):
            # If the edge connects to vertex two and doesn't connect to vertex one and edge between one and two doesn't exist
            if inc[v_two][edge] == 1 and inc[v_one][edge] == 0 and not is_duplicate_edge(inc, v_two, v_one, edge):
                # Disonnect the edge from vertex two
                inc[v_two][edge] = 0
                # Connect the edge to vertex one
                inc[v_one][edge] = 1
                break

    return inc

# Checks if graphic sequence meets the condition of containing only vertices with even degrees
# graphic_seq -> graphic sequence to be evaluated
# Returns True if condition met and False otherwise
def is_eulerian(graphic_seq):
    eulerian = True
    for vertex_degree in graphic_seq:
        if vertex_degree%2 != 0:
            eulerian = False

    return eulerian

#DEPRECATED
# Relabels vertices of a graph component to make it a standalone graph
# Gets rid of missing vertices
# component_adj_list -> adjacency list of a graph component
# component_vertex_indexes -> list of vertex labels of a graph component
# Returns relabeled adjacency list
def component_to_graph(component_adj_list, component_vertex_indexes):
    num_vertices = len(component_vertex_indexes)
    new_indexes = []
    new_adj_list = component_adj_list
    print(f'component: {component_adj_list}')
    for vertex in range(num_vertices):
        new_indexes.append(vertex+1)
        for neighbors in range(len(new_adj_list)):
            for neighbor in range(len(new_adj_list[neighbors])):
                if new_adj_list[neighbors][neighbor] == component_vertex_indexes[vertex]:
                    new_adj_list[neighbors][neighbor] = vertex+1
    print(f'graph: {new_adj_list}')
    return new_adj_list

#DEPRECATED
# Get the iterator of the largest graph component from components list
# components_list -> list of graph components which are represented by lists of member vertices
# Returns the iterator 
def get_largest_component_iterator(components_list):
    max_len = 0
    max_it = 0
    iterator = 0

    for row in components_list:
        if len(row) > max_len:
            max_len = len(row)
            max_it = iterator
        iterator += 1

    return max_it

#DEPRECATED
# Fix the "all vertex degrees even" condition of graphic sequence
def fix_graphic_seq_condition(inc, graphic_seq):
    new_graphic_seq = graphic_seq

    # For each vertex one index
    for v_one_idx in range(len(graphic_seq)):
        # If degree of vertex one is odd
        if graphic_seq[v_one_idx] % 2 != 0:
            # For each vertex two index
            for v_two_idx in range(v_one_idx+1, len(graphic_seq)):
                # If degree of vertex two is odd
                if graphic_seq[v_two_idx] % 2 != 0:
                    # Rewire an edge between rows of vertex one and two which are both odd
                    # graph_print(MatrixRepresentation.IncidenceMatrix, inc, 'inc')
                    inc = rewire_edge(inc, v_one_idx, v_two_idx)
                    # graph_print(MatrixRepresentation.IncidenceMatrix, inc, 'inc')
                    new_graphic_seq = calculate_graphic_seq_from_incidence(inc, len(graphic_seq))
                    break
    
    return [inc, new_graphic_seq]

#DEPRECATED
# Generate a random graph with even number of edges
# Graph has vertices in range of [min_vert, max_vert]
# Graph has edges in range of [min_edges, max_edges]
# min_vert -> minimum number of vertices
# max_vert -> maximum number of vertices
# min_edges -> minimum number of edges
# max_edges -> maximum number of edges
# Returns the graph as adjacency list
def get_random_eulerian_candidate(min_vert, max_vert, min_edges, max_edges):
    rng.seed()

    num_vertices = rng.randint(min_vert, max_vert+1)
    num_edges = -1
    while num_edges%2 != 0:
        num_edges = rng.randint(min_edges, max_edges+1)

    return matconv.adjacency_matrix_to_list(rngraph.random_graph_edges(num_vertices, num_edges))

#DEPRECATED
# Finds and relabels the largest component of a graph
# adj_list -> graph as adjacency list
# Returns largest component as adjacency list
def get_candidates_largest_component(adj_list):
    # Parse graph into connected components and find the largest one 
    components_list = largcomp.components(adj_list)
    largest_iterator = get_largest_component_iterator(components_list)
    largest_component = components_list[largest_iterator]

    # Get largest components adjacency list and list of vertex labels
    largest_adj_list = []
    largest_component_vertex_indexes = []
    for vertex in largest_component:
        largest_component_vertex_indexes.append(vertex)
        largest_adj_list.append(adj_list[vertex-1])

    return component_to_graph(largest_adj_list, largest_component_vertex_indexes)

# Generates a eulerian graph
# Graph has vertices in range of [min_vert, max_vert]
# Graph is randomized through edge swaps up to 'num_shuffles' times
# ^ Check edrng.randomize_edges
# min_vert -> minimum number of vertices
# max_vert -> maximum number of vertices
# num_shuffles -> target number of edge swaps
# Returns a list [inc, shuffles_done, is_fully_randomized]
# inc -> incidence matrix of the graph
# shuffles_done -> number of edge swaps executed
# is_fully_randomized -> True/False: has it been randomized 'num_shuffles' times. 
def get_random_eulerian_graph(min_vert, max_vert, num_shuffles):
    while True:
        num_vertices = rng.randint(min_vert, max_vert)
        graph_seq = []

        for _ in range(num_vertices):
            val = rng.randint(1, floor(num_vertices/2) - 1) * 2
            graph_seq.append(val)

        adj = is_graphic_sequence(graph_seq)
        if adj is not False:
            components_list = components(matconv.adjacency_matrix_to_list(adj))

            if len(components_list) == 1: 
                [inc, shuffles_done, is_fully_randomized] = edrng.randomize_edges(adj, num_shuffles)
                if shuffles_done > 0: break

    return [inc, shuffles_done, is_fully_randomized]

# Removes an edge from adjacency list of a graph
# The edge is removed between v_one and another vertex specified by it's index in v_one's neighbors
# adj_list -> adjacency list of a graph
# v_one -> vertex number in adjacency list 
# other_vertex_idx -> index of the vertex, in v_one row, the edge to which is going to be removed
def remove_edge(adj_list, v_one, other_vertex_idx):
    # Fetch vertex two number in adjacency list
    v_two = adj_list[v_one-1][other_vertex_idx]
    # Remove vertex two from neighbors list of vertex one
    adj_list[v_one-1].remove(v_two)
    # Remove vertex one from neighbors list of vertex two
    adj_list[v_two-1].remove(v_one)

# Finds the eulerian cycle in a eulerian graph
# using Hierholzer's algorithm
# adj_list -> eulerian graph as adjacency list
# Returns an array containing the cycle  
def find_eulerian_cycle(adj_list):
    temp_list = adj_list

    # Operate as stacks
    current_tour = []
    eulerian_cycle = []

    # Start current tour at vertex number 1
    current_tour.append(1)

    while len(current_tour) > 0:
        # Set current vertex as the last in current tour
        current_vertex = current_tour.pop()
        current_tour.append(current_vertex)

        # If current vertex has no neighbors 
        # remove it from current tour and add it to cycle,
        # otherwise append its first neighbor to current tour and remove the edge between them
        if len(temp_list[current_vertex-1]) == 0:
            eulerian_cycle.append(current_tour.pop())
        else:
            current_tour.append(temp_list[current_vertex-1][0])
            remove_edge(temp_list, current_vertex, 0)

    return eulerian_cycle

def test_eulerian_cycle(filename=None, min_vert=20, max_vert=50, num_shuffles=100, plots=None):
    if min_vert == None: min_vert = 20
    if max_vert == None: max_vert = 50
    if num_shuffles == None: num_shuffles = 100

    if plots == None or plots == 'y':
        plots = True
    elif plots == 'n':
        plots = False

    inc = []
    while len(inc) < 2:
        if filename == None:
            [inc, shuffles_done, is_fully_randomized] = get_random_eulerian_graph(min_vert, max_vert, num_shuffles)
            print(f'Wykonane zamiany krawedzi: {shuffles_done}')
            while shuffles_done == 0:
                print("Randomization unsuccessful!")
                [inc, shuffles_done, is_fully_randomized] = get_random_eulerian_graph(min_vert, max_vert, num_shuffles)
        else:
            [input_graph, input_representation] = read_matrix_from_file(filename)
            inc = input_representation.convert_func(MatrixRepresentation.IncidenceMatrix)(input_graph)

        if len(inc) == 0: 
            print("Generation or input failed!")
            continue

        graphic_seq = calculate_graphic_seq_from_incidence(inc, len(inc))
        print("Ciag graficzny grafu: ", graphic_seq)
        if is_eulerian(graphic_seq):
            adj_list = matconv.incidence_matrix_to_list(inc)
            eulerian_cycle = find_eulerian_cycle(adj_list)
            if eulerian_cycle[0] != eulerian_cycle[-1]:
                print("Nie znaleziono cyklu Eulera: ", eulerian_cycle)
            else:
                print("Cykl Eulera: ", eulerian_cycle)

            if plots:
                graph = icreate.create_igraph_from_incidence_matrix(inc)
                plot.plot_igraph_on_circle(graph)
        else:
            print("Graf nie jest Eulerowski")
            if plots:
                graph = icreate.create_igraph_from_incidence_matrix(inc)
                plot.plot_igraph_on_circle(graph)