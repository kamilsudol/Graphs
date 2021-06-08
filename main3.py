from Arguments import ArgumentsSingleton
from lib.Project_3.random_weighted_graph import generate_random_weighted_graph_adjacency
from lib.Project_3.weighted_graph import plot_weighted_graph_on_circle
from lib.Project_3.dijkstras import dijkstra_find_and_print_shortest_paths
from lib.Project_3.dijkstras import print_shortest_paths_table
from lib.Project_3.dijkstras import print_graph_centers
from lib.Project_3.spanning_tree import draw_minimum_spanning_tree
from lib.Utils.decorators import retry_on_value_error
from lib.Utils.pretty_print import print_int_matrix

# TODO indentation in 2 - path printing
# TODO sum of all edges in spanning tree
# TODO plot both graphs in spanning tree


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
        raise ValueError("Nie ma takiego zadania")

    return index


def randomize_and_plot_graph(arg_singleton):
    args = arg_singleton.get_instance().arguments

    graph_adjacency_matrix = generate_random_weighted_graph_adjacency(arg_singleton)
    
    while not graph_adjacency_matrix:
        print('Blad generowania grafu. Sprobuj jeszcze raz.')
        graph_adjacency_matrix = generate_random_weighted_graph_adjacency(arg_singleton)

    if args['plots'] != 'n':
        plot_weighted_graph_on_circle(graph_adjacency_matrix)

    print('Wygenerowano graf o nastepujacej macierzy sasiedztwa:')
    print_int_matrix(graph_adjacency_matrix)

    return graph_adjacency_matrix


if __name__ == '__main__':
    arg_singleton = ArgumentsSingleton()
    args = arg_singleton.get_instance().arguments
    
    run_from_cl = False
    exercises = [
        randomize_and_plot_graph,
        dijkstra_find_and_print_shortest_paths,
        print_shortest_paths_table,
        print_graph_centers,
        draw_minimum_spanning_tree
    ]
    graph_adjacency_matrix = None

    try:
        if args['task'] is not None:
            task = args['task']
            tasks = [1, 2, 3, 4, 5]
            tasks.index(task)

            run_from_cl = True
    except ValueError:
        print("Invalid task")

    while not run_from_cl:
        exercise_index = get_exercise_index()
        if exercise_index == len(exercises):
            break
        else:
            if exercise_index != 0 and not graph_adjacency_matrix:
                print('Blad: Graf nie zostal jeszcze wygenerowany. Wpisz \'1\' aby wygenerowac graf.\n')
            elif exercise_index == 0:
                graph_adjacency_matrix = retry_on_value_error(
                    lambda: exercises[exercise_index](arg_singleton)
                )()
            else:
                retry_on_value_error(
                    lambda: exercises[exercise_index](graph_adjacency_matrix, arg_singleton)
                )()

    try:
        if run_from_cl:
            if args['task'] == 1: 
                graph_adjacency_matrix = exercises[args['task']-1](arg_singleton)
            else: 
                if graph_adjacency_matrix is None:
                    initial_plot = args['plots']
                    args['plots'] = 'n'
                    graph_adjacency_matrix = randomize_and_plot_graph(arg_singleton)
                    args['plots'] = initial_plot

                exercises[args['task']-1](graph_adjacency_matrix, arg_singleton)
                if args['plots'] != 'n':
                    plot_weighted_graph_on_circle(graph_adjacency_matrix)
    except ValueError as e:
        print("Wystąpił błąd\n")
        print(e)
