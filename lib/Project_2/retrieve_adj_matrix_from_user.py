from .graphic_sequence import load_sequence, is_graphic_sequence
from lib.Project_1.MatrixRepresentation import MatrixRepresentation
from lib.Project_1.matrix_conversions import incidence_matrix_to_adjacency_matrix, list_to_adjacency_matrix
from lib.Project_1.random_graph import random_graph_edges, random_graph_probability
from lib.Project_1.read_data import read_matrix_from_file


# reading graph from file as an adjacency matrix
def graph_file_read():
    filename = input(
        "Wskaż nazwę pliku zawierającego macierz w formie\n - listy sąsiedztwa\n - macierzy incydencji\n - macierzy sąsiedztwa\n> ")

    matrix, matrix_representation = read_matrix_from_file(filename)
    print("Wykryto " + matrix_representation.to_string())

    return any_representation_to_adjacency_matrix(matrix, matrix_representation)


# converting any graph representation to adjacency matrix
def any_representation_to_adjacency_matrix(matrix, matrix_representation):
    if matrix_representation == MatrixRepresentation.List:
        return list_to_adjacency_matrix(matrix)
    elif matrix_representation == MatrixRepresentation.AdjacencyMatrix:
        return matrix
    elif matrix_representation == MatrixRepresentation.IncidenceMatrix or matrix_representation == MatrixRepresentation.UndeterminedMatrix:
        return incidence_matrix_to_adjacency_matrix(matrix)
    return None


def retrieve_adjacency_matrix_from_user():
    try:
        input_type = int(input('Wpisz 1 aby podac plik zawierajacy dowolna reprezentacje grafu.\n'
                               'Wpisz 2 aby wylosowac graf G(n, l).\n'
                               'Wpisz 3 aby wylosowac graf G(n, p).\n'
                               'Wpisz 4 aby wczytac graf z ciagu graficznego\n').strip())
    except ValueError:
        print('Blad: podano niepoprawna wartosc.')
        raise ValueError
    except KeyboardInterrupt:
        raise ValueError

    if input_type == 1:
        return graph_file_read()
    elif input_type == 2:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        ne = int(input('Podaj ilosc krawedzi: ').strip())
        return random_graph_edges(nv, ne)
    elif input_type == 3:
        nv = int(input('Podaj ilosc wezlow: ').strip())
        p = float(input('Podaj prawdopodobienstwo istnienia krawedzi: ').strip())
        return random_graph_probability(nv, p)
    elif input_type == 4:
        seq = load_sequence()
        result = is_graphic_sequence(seq)
        if result is not False:
            print("Ciag jest graficzny")
            return result
        else:
            print("Ciag nie jest graficzny")
            raise ValueError
    else:
        print('Wybrano niepoprawna opcje.')
        raise ValueError
