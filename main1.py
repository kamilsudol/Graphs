from lib.Project_1.read_data import read_matrix_from_file, graph_print
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from lib.Project_1.random_graph import graph_randomizer_start


close = lambda: None


def graph_conversion_start(flag=False):
    filename = input(
        "Wskaż nazwę pliku zawierającego macierz w formie\n - listy sąsiedztwa\n - macierzy incydencji\n - macierzy sąsiedztwa\n> ")

    matrix, matrix_representation = read_matrix_from_file(filename)
    print("Wykryto " + matrix_representation.to_string())

    if flag:
        return matrix, matrix_representation

    graph_print(matrix_representation, matrix)


def graph_visualisation_start():
    matrix, matrix_representation = graph_conversion_start(True)
    graph = matrix_representation.to_igraph_func()(matrix)
    plot_igraph_on_circle(graph)


if __name__ == '__main__':
    exercises = [graph_conversion_start, graph_visualisation_start, graph_randomizer_start, close]

    while True:
        try:
            exercise_index = int(input(
                "Wybierz funkcje:\n - 1 - konwertuj reprezentacje grafu\n - 2 - wizualizuj graf \n - 3 - generuj "
                "graf losowy\n - 4 - zakoncz\n").strip()) - 1
            exercises[exercise_index]()
            if exercise_index == 3:
                break
            print()
        except ValueError:
            print("Wystąpił błąd\n")
