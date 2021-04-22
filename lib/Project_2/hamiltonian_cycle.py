import sys

from lib.Project_1.MatrixRepresentation import MatrixRepresentation
from lib.Project_1.matrix_conversions import incidence_matrix_to_adjacency_matrix, list_to_adjacency_matrix, adjacency_matrix_to_list
from lib.Project_1.random_graph import random_graph_edges, random_graph_probability
from lib.Project_1.read_data import read_matrix_from_file
from .largest_connected_component import components


def any_representation_to_adjacency_matrix(matrix, matrix_representation):
    if matrix_representation == MatrixRepresentation.List:
        return list_to_adjacency_matrix(matrix)
    elif matrix_representation == MatrixRepresentation.AdjacencyMatrix:
        return matrix
    elif matrix_representation == MatrixRepresentation.IncidenceMatrix:
        return incidence_matrix_to_adjacency_matrix(matrix)
    return None


def get_adjacency_matrix_from_file():
    filename = input('Podaj nazwe pliku: ').strip()
    matrix, matrix_representation = read_matrix_from_file(filename)
    return any_representation_to_adjacency_matrix(matrix, matrix_representation)


def retrieve_adjacency_matrix_from_user():
    try:
        input_type = int(input('Wpisz 1 aby podac plik zawierajacy dowolna reprezentacje grafu.\n'
                           'Wpisz 2 aby wylosowac graf G(n, l).\n'
                           'Wpisz 3 aby wylosowac graf G(n, p).\n').strip())
    except ValueError:
        print('Blad: podano niepoprawna wartosc.')
        sys.exit(1)
    except KeyboardInterrupt:
        print('Zamykanie programu...')
        sys.exit(0)

    if input_type == 1:
        return get_adjacency_matrix_from_file()
    elif input_type == 2:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        ne = int(input('Podaj ilosc krawedzi: ').strip())
        return random_graph_edges(nv, ne)
    elif input_type == 3:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        p = float(input('Podaj prawdopodobienstwo istnienia krawedzi').strip())
        return random_graph_probability(nv, p)
    else:
        print('Wybrano niepoprawna opcje.')


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
