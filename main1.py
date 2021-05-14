from lib.Project_1.read_data import read_matrix_from_file, graph_print
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from lib.Project_1.random_graph import graph_randomizer_start
from Arguments_Project_1 import ArgumentsSingleton
from lib.Utils.decorators import retry_on_value_error

close = lambda: None


@retry_on_value_error
def get_exercise_index():
    index = int(input(
        "Wybierz funkcje:\n"
        " - 1 - konwertuj reprezentacje grafu\n"
        " - 2 - wizualizuj graf \n"
        " - 3 - generuj graf losowy\n"
        " - 4 - zakoncz\n").strip()) - 1

    if index < 0 or index > 3:
        raise ValueError

    return index


def graph_conversion_start(flag=False, filename=None, output=None):
    if filename is None:
        filename = input(
            "Wskaż nazwę pliku zawierającego macierz w formie\n - listy sąsiedztwa\n - macierzy incydencji\n - macierzy sąsiedztwa\n> ")

        matrix, matrix_representation = read_matrix_from_file(filename)
        print("Wykryto " + matrix_representation.to_string())
    else:
        matrix, matrix_representation = read_matrix_from_file(filename)

    if flag:
        return matrix, matrix_representation

    graph_print(matrix_representation, matrix, output)


def graph_visualisation_start(filename=None):
    matrix, matrix_representation = graph_conversion_start(flag=True, filename=filename)
    graph = matrix_representation.to_igraph_func()(matrix)
    plot_igraph_on_circle(graph)


if __name__ == '__main__':
    arg_singleton = ArgumentsSingleton()
    args = arg_singleton.get_instance().arguments
    exercises = [graph_conversion_start, graph_visualisation_start, graph_randomizer_start, close]

    run_from_cl = False

    try:
        if args['task'] is not None:
            task = args['task']
            tasks = [1, 2, 3]
            tasks.index(task)

            run_from_cl = True
    except ValueError:
        print("Invalid task")

    while not run_from_cl:
        try:
            exercise_index = get_exercise_index()
            exercises[exercise_index]()
            if exercise_index == 3:
                break
            print()
        except ValueError:
            print("Wystąpił błąd!\n")

    try:
        if run_from_cl:
            if task == 1:
                exercises[task - 1](filename=args['filename'], output=args['output'])
            elif task == 2:
                exercises[task - 1](args['filename'])
            elif task == 3:
                exercises[task - 1](output=args['output'], num_vertices=args['vertices'],
                                    probability=args['probability'], num_edges=args['edges'], plot=args['plots'])
            else:
                print('Wprowadzono nieproprawne argumenty!')
    except ValueError:
        print("Wystąpił błąd!\n")
