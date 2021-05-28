from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
from .largest_connected_component import components
from .retrieve_adj_matrix_from_user import retrieve_adjacency_matrix_from_user
from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from lib.Project_1.read_data import read_matrix_from_file
from lib.Project_1.MatrixRepresentation import MatrixRepresentation


def hamil_check_neighbours(path, adjacency_matrix, pos, n_nodes):
    current_neighbours = [i for i in range(n_nodes) if adjacency_matrix[path[pos]][i]]
    if pos == n_nodes - 1:
        if path[0] in current_neighbours:
            return path
        else:
            return []

    for k in current_neighbours:
        if k not in path:
            path[pos + 1] = k
            if hamil_check_neighbours(path, adjacency_matrix, pos + 1, n_nodes):
                return path
    path[pos + 1] = 0
    return []


def find_hamiltonian_cycle(filename=None, plot=None):
    if filename is None:
        adjacency_matrix = retrieve_adjacency_matrix_from_user()
    else:
        matrix, rep = read_matrix_from_file(filename)
        adjacency_matrix = rep.convert_func(MatrixRepresentation.AdjacencyMatrix)(matrix)
    list_matrix = adjacency_matrix_to_list(adjacency_matrix)
    if len(components(list_matrix)) != 1:
        print('Graf nie jest hamiltonowski.')
        return
    n_nodes = len(adjacency_matrix)
    print(adjacency_matrix)
    path = hamil_check_neighbours([0 for _ in range(n_nodes)], adjacency_matrix, 0, n_nodes)
    if not path:
        print('Graf nie jest hamiltonowski.')
    else:
        print('Znaleziono cykl hamiltona: ', end='')
        print(list(map(lambda i: i+1, path)))
        graph = create_igraph_from_adjacency_matrix(adjacency_matrix)
        if plot is None or plot == 'y':
            plot_igraph_on_circle(graph)
