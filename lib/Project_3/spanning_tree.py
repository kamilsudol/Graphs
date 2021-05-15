from lib.Project_3.weighted_graph import plot_weighted_graph_on_circle
from lib.Project_2.largest_connected_component import components
from lib.Project_1.matrix_conversions import adjacency_matrix_to_list


def intersection(list1, list2):
    return [v for v in list1 if v in list2]


def prim_generate_minimum_spanning_tree(adjacency_matrix):
    size = len(adjacency_matrix)
    res = [[0] * size for _ in range(size)]

    ready_vertices = [0]
    free_vertices = [i for i in range(1, size)]

    while len(ready_vertices) < size:
        current_row = [int(v) for v in adjacency_matrix[ready_vertices[-1]]]
        neighbours = [i for i, v in enumerate(current_row) if v != 0]
        available_neighbours = intersection(neighbours, free_vertices)
        min_index = current_row.index(min([current_row[i] for i in available_neighbours]))

        res[ready_vertices[-1]][min_index] = current_row[min_index]
        res[min_index][ready_vertices[-1]] = current_row[min_index]
        ready_vertices.append(min_index)
        free_vertices.remove(min_index)

    return res


def draw_minimum_spanning_tree(adjacency_matrix):
    adjacency_list = adjacency_matrix_to_list(adjacency_matrix)
    if len(components(adjacency_list)) > 1:
        print('Blad genracji minimalnego drzewa rozpinajacego: graf nie jest spojny')
        return []
    res_adj_mat = prim_generate_minimum_spanning_tree(adjacency_matrix)
    plot_weighted_graph_on_circle(res_adj_mat)
