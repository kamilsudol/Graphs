from graphic_sequence import test_graphic_sequence
from edge_randomizer import test_randomization
from random_k_connected_graph import generate_and_show_random_k_connected_graph
from largest_connected_component import find_largest_connected_component


do_nothing = lambda : None
exercises = [test_graphic_sequence, test_randomization, find_largest_connected_component, do_nothing, generate_and_show_random_k_connected_graph]

while True:
    exercise_index = int(input("Wybierz funkcje:\n - 1 - rysuj ciag graficzny\n - 2 - przeprowadz randomizacje grafu \n - 3 - znajdz najwieksze spojne skladowe na grafie\n - \n - 5 - generuj losowy graf k-spojny\n> ").strip()) - 1
    exercises[exercise_index]()
    print()