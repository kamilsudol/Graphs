from lib.Project_2.graphic_sequence import test_graphic_sequence
from lib.Project_2.edge_randomizer import test_randomization
from lib.Project_2.random_k_connected_graph import generate_and_show_random_k_connected_graph
from lib.Project_2.largest_connected_component import find_largest_connected_component
from lib.Project_2.hamiltonian_cycle import find_hamiltonian_cycle
from lib.Project_2.eulerian_cycle import test_eulerian_cycle
from lib.Utils.decorators import retry_on_value_error


@retry_on_value_error
def get_exercise_index():
    index = int(input(
        "Wybierz funkcje:\n"
        " - 1 - rysuj ciag graficzny\n"
        " - 2 - przeprowadz randomizacje grafu\n"
        " - 3 - znajdz najwieksza spojna skladowa na grafie\n"
        " - 4 - generuj losowy graf eulerowski i znajdz na nim cykl eulera\n"
        " - 5 - generuj losowy graf k-spojny\n"
        " - 6 - sprawdz czy graf jest hamiltonowski\n"
        " - 7 - zakoncz\n> ").strip()) - 1

    if index < 0 or index > 6:
        raise ValueError 

    return index


if __name__ == '__main__':
    exercises = [test_graphic_sequence, test_randomization, find_largest_connected_component, test_eulerian_cycle,
                 generate_and_show_random_k_connected_graph, find_hamiltonian_cycle]

    while True:
        exercise_index = get_exercise_index()
        if exercise_index == len(exercises):
            break

        retry_on_value_error(
            lambda : exercises[exercise_index]()
        )()

        print()