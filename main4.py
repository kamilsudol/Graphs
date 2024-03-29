from lib.Project_4.random_digraph import digraph_randomizer_start
from lib.Project_4.strongly_connected_component import test_strongly_connected
from lib.Project_4.bellman_ford import bellman_ford_start
from lib.Project_4.johnson import paths_between_nodes
from lib.Utils.decorators import retry_on_value_error
from Arguments import ArgumentsSingleton


@retry_on_value_error
def get_exercise_index():
    index = int(input(
        "Wybierz funkcje:\n"
        " - 1 - losuj graf skierowany\n"
        " - 2 - znajdz najwieksza silnie spojna skladowa\n"
        " - 3 - znajdz najkrotsze sciezki od danego wierzcholka\n"
        " - 4 - odleglosci pomiedzy wszystkimi parami wierzcholkow\n"
        " - 5 - zakoncz\n> ").strip()) - 1

    if index < 0 or index > 4:
        raise ValueError("Nie ma takiego zadania")

    return index

do_nothing = lambda: None

if __name__ == '__main__':
    arg_singleton = ArgumentsSingleton()
    args = arg_singleton.get_instance().arguments
    
    run_from_cl = False
    exercises = [digraph_randomizer_start, test_strongly_connected, bellman_ford_start, paths_between_nodes]

    try:
        if args['task'] is not None:
            task = args['task']
            tasks = [1, 2, 3, 4]
            tasks.index(task)

            run_from_cl = True
    except ValueError:
        print("Invalid task")

    while not run_from_cl:
        exercise_index = get_exercise_index()
        if exercise_index == len(exercises):
            break

        retry_on_value_error(
            lambda : exercises[exercise_index](arg_singleton)
        )()

        print()

    try:
        if run_from_cl:
            exercises[args['task']-1](arg_singleton)
    except ValueError as e:
        print("Wystąpił błąd\n")
        print(e)