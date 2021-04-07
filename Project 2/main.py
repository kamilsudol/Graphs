from graphic_sequence import test_graphic_sequence
from random_k_connected_graph import generate_and_show_random_k_connected_graph

do_nothing = lambda : None
exercises = [test_graphic_sequence, do_nothing, do_nothing, do_nothing, generate_and_show_random_k_connected_graph]

while True:
    exercise_index = int(input("Wybierz funkcje:\n - 1 - rysuj ciag graficzny\n - \n - \n - \n - 5 - generuj losowy graf k-spojny\n> ").strip()) - 1
    exercises[exercise_index]()
    print()