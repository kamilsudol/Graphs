from igraph import *

from lib.Project_3.random_weighted_graph import generate_random_weighted_graph_adjacency
from lib.Project_3.weighted_graph import plot_weighted_graph_on_circle
from lib.Project_3.dijkstras import dijkstra_find_and_print_shortest_paths
from lib.Project_3.dijkstras import print_shortest_paths_table
from lib.Project_3.dijkstras import print_graph_centers
from lib.Project_3.spanning_tree import draw_minimum_spanning_tree
from lib.Utils.decorators import retry_on_value_error


@retry_on_value_error
def get_exercise_index():
    index = int(input(
        'Wybierz funkcje:\n'
        ' - 1 - Generuj spojny graf losowy z krawedziami o losowych wagach\n'
        ' - 2 - Wypisz najkrotsze sciezki w grafie (algorytm Dijkstry)\n'
        ' - 3 - Wyznacz macierz odleglosci miedzy wszystkimi parami wierzcholkow\n'
        ' - 4 - Wyznacz centrum i centrum minmax grafu\n'
        ' - 5 - Wyznacz minimalne drzewo rozpinajace\n'
        ' - 6 - Zakoncz\n> ').strip()) - 1

    if index < 0 or index > 5:
        raise ValueError 

    return index


def randomize_and_plot_graph():
    graph_adjacency_matrix = generate_random_weighted_graph_adjacency()
    
    while not graph_adjacency_matrix:
        print('Blad generowania grafu. Sprobuj jeszcze raz.')
        graph_adjacency_matrix = generate_random_weighted_graph_adjacency()
    plot_weighted_graph_on_circle(graph_adjacency_matrix)

    return graph_adjacency_matrix


if __name__ == '__main__':
    exercises = [
        randomize_and_plot_graph,
        dijkstra_find_and_print_shortest_paths,
        print_shortest_paths_table,
        print_graph_centers,
        draw_minimum_spanning_tree
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
                graph_adjacency_matrix = retry_on_value_error(
                    lambda: exercises[exercise_index]()
                )()
            else:
                retry_on_value_error(
                    lambda: exercises[exercise_index](graph_adjacency_matrix)
                )()
