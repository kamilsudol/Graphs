from Arguments import ArgumentsSingleton
from lib.Project_2.graphic_sequence import test_graphic_sequence
from lib.Project_2.edge_randomizer import test_randomization
from lib.Project_2.random_k_connected_graph import generate_and_show_random_k_connected_graph
from lib.Project_2.largest_connected_component import find_largest_connected_component
from lib.Project_2.hamiltonian_cycle import find_hamiltonian_cycle
from lib.Project_2.eulerian_cycle import test_eulerian_cycle


def close():
    return

do_nothing = lambda: None

if __name__ == '__main__':
    arg_singleton = ArgumentsSingleton()
    args = arg_singleton.get_instance().arguments

    run_from_cl = False

    try:
        if args['task'] is not None:

            task = args['task']
            tasks = [1, 2, 3, 4, 5, 6]
            tasks.index(task)

            run_from_cl = True
    except ValueError:
        print("Invalid task")

    exercises = [test_graphic_sequence, test_randomization, find_largest_connected_component, test_eulerian_cycle,
                 generate_and_show_random_k_connected_graph, find_hamiltonian_cycle, close]

    while not run_from_cl:
        try:
            exercise_index = int(input(
                "Wybierz funkcje:\n - 1 - rysuj ciag graficzny\n - 2 - przeprowadz randomizacje grafu \n - 3 - znajdz "
                "najwieksza spojna skladowa na grafie\n - 4 - generuj losowy graf eulerowski i znajdz na nim cykl eulera\n - 5 - generuj losowy graf k-spojny\n - 6 - sprawdz czy "
                "graf jest hamiltonowski\n - 7 - zakoncz\n> ").strip()) - 1
            exercises[exercise_index]()
            if exercise_index == 6:
                break
            print()
        except ValueError:
            print("Wystąpił błąd\n")

    if run_from_cl:
        if task == 1:
            exercises[task - 1](args['plots'])
        elif task == 2:
            exercises[task - 1](args['filename'], args['output'], args['shuffles'], args['plots'])
        elif task == 3:
            exercises[task - 1](args['filename'], args['plots'])
        elif task == 4:
            exercises[task - 1](args['filename'], args['minv'], args['maxv'], args['shuffles'], args['plots'])
        elif task == 5:
            exercises[task - 1](args['vertices'], args['regularity'])
        elif task == 6:
            exercises[task - 1](args['filename'], args['plots'])
        else:
            print('Can\'t run this from command line')
