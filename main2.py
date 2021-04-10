from lib.Project_2.graphic_sequence import test_graphic_sequence
from lib.Project_2.edge_randomizer import test_randomization
from lib.Project_2.random_k_connected_graph import generate_and_show_random_k_connected_graph
from lib.Project_2.largest_connected_component import find_largest_connected_component
from lib.Project_2.hamiltonian_cycle import find_hamiltonian_cycle


do_nothing = lambda: None

if __name__ == '__main__':
    exercises = [test_graphic_sequence, test_randomization, find_largest_connected_component, do_nothing,
                 generate_and_show_random_k_connected_graph, find_hamiltonian_cycle]

    while True:
        try:
            exercise_index = int(input(
                "Wybierz funkcje:\n - 1 - rysuj ciag graficzny\n - 2 - przeprowadz randomizacje grafu \n - 3 - znajdz "
                "najwieksze spojne skladowe na grafie\n - \n - 5 - generuj losowy graf k-spojny\n - 6 - sprawdz czy "
                "graf jest hamiltonowski\n> ").strip()) - 1
            exercises[exercise_index]()
            print()
        except ValueError:
            print("Wystąpił błąd\n")
