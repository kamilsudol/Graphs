from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from .largest_connected_component import components
from .retrieve_adj_matrix_from_user import retrieve_adjacency_matrix_from_user
from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle


def hamil_check_neighbours(path, adjacency_matrix, pos, n_nodes):
    current_neighbours = [i for i in range(n_nodes) if adjacency_matrix[pos][i]]
    if pos == n_nodes - 1 and path[0] in current_neighbours:
        return path

    for k in current_neighbours:
        if k not in path:
            path[pos + 1] = k
            if hamil_check_neighbours(path, adjacency_matrix, pos + 1, n_nodes):
                return path
    return []


def find_hamiltonian_cycle():
    adjacency_matrix = retrieve_adjacency_matrix_from_user()
    list_matrix = adjacency_matrix_to_list(adjacency_matrix)
    if len(components(list_matrix)) != 1:
        print('Graf nie jest hamiltonowski.')
        return
    n_nodes = len(adjacency_matrix)
    path = hamil_check_neighbours([0 for _ in range(n_nodes)], adjacency_matrix, 0, n_nodes)
    if not path:
        print('Graf nie jest hamiltonowski.')
    else:
        print('Znaleziono cykl hamiltona: ', end='')
        print(list(map(lambda i: i+1, path)))
        graph = create_igraph_from_adjacency_matrix(adjacency_matrix)
        plot_igraph_on_circle(graph)
