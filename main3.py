from igraph import *

from lib.Project_3.random_weighted_graph import generate_random_weighted_graph_adjacency
from lib.Project_3.weighted_graph import create_weighted_igraph_from_adjacency
from lib.Project_3.weighted_graph import plot_weighted_igraph_on_circle


def do_nothing():
    pass


def get_exercise_index():
    try:
        index = int(input(
            'Wybierz funkcje:\n'
            ' - 1 - Generuj spojny graf losowy z krawedziami o losowych wagach\n'
            ' - 2 - Wypisz najkrotsze sciezki w grafie (algorytm Dijkstry)\n'
            ' - 3 - Wyznacz macierz odleglosci miedzy wszystkimi parami wierzcholkow\n'
            ' - 4 - Wyznacz centrum i centrum minmax grafu\n'
            ' - 5 - Wyznacz minimalne drzewo rozpinajace\n'
            ' - 6 - Zakoncz\n').strip()) - 1
        return index
    except ValueError:
        print('Blad: podano niepoprawna wartosc.')
        return get_exercise_index()
    except KeyboardInterrupt:
        print('Zamykanie programu...')
        sys.exit(0)


if __name__ == '__main__':
    exercises = [
        generate_random_weighted_graph_adjacency,
        do_nothing,
        do_nothing,
        do_nothing,
        do_nothing
    ]
    graph_adjacency_matrix = None

    while True:
        exercise_index = get_exercise_index()
        if exercise_index == len(exercises):
            break
        else:
            if exercise_index != 0 and not graph_adjacency_matrix:
                print('Blad: Graf nie zostal jeszcze wygenerowany. Wpisz \'1\' aby wygenerowac graf.\n')
            elif exercise_index == 0:
                graph_adjacency_matrix = generate_random_weighted_graph_adjacency()
                g = create_weighted_igraph_from_adjacency(graph_adjacency_matrix)
                plot_weighted_igraph_on_circle(g)
            else:
                exercises[exercise_index](graph_adjacency_matrix)
