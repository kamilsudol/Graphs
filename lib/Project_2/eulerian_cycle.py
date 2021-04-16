import lib.Project_1.matrix_conversions as matconv
import lib.Project_1.random_graph as rngraph
import lib.Project_1.igraph_creation as icreate
import lib.Project_1.plot_igraph_on_circle as plot
from . import edge_randomizer as edrng
from . import largest_connected_component as largcomp
import random as rng


def is_duplicate_edge(inc, v_one, v_two, checked_edge):
    [vertex_one_checked, _] = edrng.find_vertices(len(inc), inc, checked_edge)
    vertex_two_checked = v_two
    for edge in range(len(inc[v_one])):
        if edge != checked_edge:
            [vertex_one_temp, vertex_two_temp] = edrng.find_vertices(len(inc), inc, edge)

            if vertex_one_checked == vertex_one_temp and vertex_two_checked == vertex_two_temp:
                return True
    return False

def calculate_graphic_seq_from_incidence(inc, num_vertices):
    graphic_seq = []
    vertex_degree = 0

    for row in range(num_vertices):
        for vertex in inc[row]:
            vertex_degree += vertex
        graphic_seq.append(vertex_degree)
        vertex_degree = 0
    
    return graphic_seq

def rewire_edge(inc, v_one, v_two):
    v_one_deg = 0
    v_two_deg = 0

    for edge in range(len(inc[v_one])):
        v_one_deg += inc[v_one][edge]
        v_two_deg += inc[v_two][edge]

    if v_one_deg > v_two_deg:
        for edge in range(len(inc[v_one])):
            if inc[v_one][edge] == 1 and inc[v_two][edge] == 0 and not is_duplicate_edge(inc, v_one, v_two, edge):
                inc[v_one][edge] = 0
                inc[v_two][edge] = 1
                break
    else:
        for edge in range(len(inc[v_two])):
            if inc[v_two][edge] == 1 and inc[v_one][edge] == 0 and not is_duplicate_edge(inc, v_two, v_one, edge):
                inc[v_two][edge] = 0
                inc[v_one][edge] = 1
                break

    return inc

def is_eulerian(graphic_seq):
    eulerian = True
    for vertex_degree in graphic_seq:
        if vertex_degree%2 != 0:
            eulerian = False

    return eulerian

def component_to_graph(component_adj_list, component_vertex_indexes):
    num_vertices = len(component_vertex_indexes)
    new_indexes = []
    new_adj_list = component_adj_list

    for vertex in range(num_vertices):
        new_indexes.append(vertex+1)
        for neighbors in range(len(new_adj_list)):
            for neighbor in range(len(new_adj_list[neighbors])):
                if new_adj_list[neighbors][neighbor] == component_vertex_indexes[vertex]:
                    new_adj_list[neighbors][neighbor] = vertex+1
    
    return new_adj_list

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

def fix_graphic_seq_condition(inc, graphic_seq):
    new_graphic_seq = graphic_seq

    for v_one_idx in range(len(graphic_seq)):
        if graphic_seq[v_one_idx] % 2 != 0:
            for v_two_idx in range(v_one_idx+1, len(graphic_seq)):
                if graphic_seq[v_two_idx] % 2 != 0:
                    inc = rewire_edge(inc, v_one_idx, v_two_idx)
                    new_graphic_seq = calculate_graphic_seq_from_incidence(inc, len(graphic_seq))
                    break
    
    return new_graphic_seq

def get_random_eulerian_candidate(min_vert, max_vert, min_edges, max_edges):
    rng.seed()

    num_vertices = rng.randint(min_vert, max_vert+1)
    num_edges = -1
    while num_edges%2 != 0:
        num_edges = rng.randint(min_edges, max_edges+1)

    return matconv.adjacency_matrix_to_list(rngraph.random_graph_edges(num_vertices, num_edges))

def get_candidates_largest_component(adj_list):
    components_list = largcomp.components(adj_list)
    largest_iterator = get_largest_component_iterator(components_list)
    largest_component = components_list[largest_iterator]

    largest_adj_list = []
    largest_component_vertex_indexes = []
    for vertex in largest_component:
        largest_component_vertex_indexes.append(vertex)
        largest_adj_list.append(adj_list[vertex-1])

    return component_to_graph(largest_adj_list, largest_component_vertex_indexes)

def get_random_eulerian_graph():
    candidate_list = get_random_eulerian_candidate(6, 15, 4, 24)

    largest_candidate_list = get_candidates_largest_component(candidate_list)
    
    graphic_seq = []
    for vertex in largest_candidate_list:
        graphic_seq.append(len(vertex))
    
    inc = matconv.list_to_incidence_matrix(largest_candidate_list)

    old_graphic_seq = []
    not_eulerian = True
    while not_eulerian:
        old_graphic_seq = graphic_seq
        graphic_seq = fix_graphic_seq_condition(inc, graphic_seq)
        if old_graphic_seq == graphic_seq:
            return []

        not_eulerian = not(is_eulerian(graphic_seq))

    return inc

def remove_edge(adj_list, v_one, other_vertex_idx):
    v_two = adj_list[v_one-1][other_vertex_idx]
    adj_list[v_one-1].remove(v_two)
    adj_list[v_two-1].remove(v_one)

def find_eulerian_cycle(adj_list):
    temp_list = adj_list

    current_tour = []
    eulerian_cycle = []

    current_tour.append(1)

    while len(current_tour) > 0:
        current_vertex = current_tour.pop()
        current_tour.append(current_vertex)

        if len(temp_list[current_vertex-1]) == 0:
            eulerian_cycle.append(current_tour.pop())
        else:
            current_tour.append(temp_list[current_vertex-1][0])
            remove_edge(temp_list, current_vertex, 0)

    return eulerian_cycle

def test_eulerian_cycle():
    inc = []
    while len(inc) < 2:
        inc = get_random_eulerian_graph()

        print("Ciag graficzny grafu eulerowskiego: ", calculate_graphic_seq_from_incidence(inc, len(inc)))

        adj_list = matconv.incidence_matrix_to_list(inc)
        print("Cykl Eulera: ", find_eulerian_cycle(adj_list))

        graph = icreate.create_igraph_from_incidence_matrix(inc)
        plot.plot_igraph_on_circle(graph)