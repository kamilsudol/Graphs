from lib.Project_4.random_digraph import digraph_randomizer_start
from lib.Project_4.strongly_connected_component import test_strongly_connected
from lib.Project_4.bellman_ford import test_2_3

do_nothing = lambda: None

if __name__ == '__main__':
    exercises = [digraph_randomizer_start, test_strongly_connected, test_2_3, do_nothing, do_nothing]

    while True:
        exercise_index = int(input(
            "Wybierz funkcje:\n"
            " - 1 - losuj graf skierowany\n"
            " - 2 - znajdz najwieksza silnie spojna skladowa\n"
            " - 3 - znajdz najkrotsza sciezke do danego wierzcholka\n"
            " - 4 - \n"
            " - 5 - zakoncz\n> ").strip()) - 1
        exercises[exercise_index]()
            
        if exercise_index == len(exercises) - 1:
            break

        print()